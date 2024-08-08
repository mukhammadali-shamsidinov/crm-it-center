from django.shortcuts import render

# Create your views here.
from django.views.generic import UpdateView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from school_management.models import Student
from school_management.serializers import StudentSerializers


class StudentAPIView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializers = StudentSerializers(students,many=True).data

        return Response(
            data={

                "data":serializers,
                "status":status.HTTP_200_OK
            }
        )

    def post(self,request):
        serializers = StudentSerializers(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(
                data=serializers.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializers.data
            )


class StudentUpdateView(APIView):
   def get(self,request,pk):
        model =  Student.objects.get(pk=pk)
        serializer =StudentSerializers(model)
        return Response(
            data=serializer.data
        )
        return Response
   def put(self,request,pk):
       instance = Student.objects.get(pk=pk)

       serializers = StudentSerializers(instance,data=request.data)

       if serializers.is_valid():
           serializers.save()
           return Response(
               data=serializers.data,
               status=status.HTTP_200_OK
           )
       else:
           return Response(
               data=serializers.errors,
               status=status.HTTP_400_BAD_REQUEST
           )
   def delete(self,request,pk):
       model = Student.objects.get(pk=pk)
       model.delete()
       return Response(
           data={
               "message":"success"
           }
       )



