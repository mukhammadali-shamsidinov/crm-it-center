from rest_framework import  serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username","first_name","last_name","email","user_role")





class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username","first_name","last_name","email","password","user_role")


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data,password=password)
        return user