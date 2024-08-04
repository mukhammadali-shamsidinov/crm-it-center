from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import CustomUser
from users.serializers import CustomUserSerializer, RegisterSerializers


class ProfileAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user, many=False)
        return Response(serializer.data)



class RegisterAPIView(APIView):
    def post(self,request):
        serializer = RegisterSerializers(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={
                    "message":False,
                    "status":status.HTTP_400_BAD_REQUEST
                }
            )


