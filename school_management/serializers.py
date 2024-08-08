from rest_framework import serializers

from school_management.models import Student


class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"