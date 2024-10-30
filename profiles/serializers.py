from rest_framework import serializers
from .models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Profile
        fields = (
            'user_email',
            'first_name',
            'last_name',
            'bio',
            'gender'
        )


