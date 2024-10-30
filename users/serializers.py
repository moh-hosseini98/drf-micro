from rest_framework import serializers
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,write_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
            'date_joined',
        )

    def create(self,validated_data):
        user = User.objects.create_user(
            **validated_data
        )    

        user.set_password(validated_data['password'])
        user.save()

        return user