from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from .serializers import UserProfileSerializer


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        profile =  self.request.user.profile
        return profile

