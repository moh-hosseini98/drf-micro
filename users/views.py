from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

from .serializers import RegisterSerializer
from .models import User



class RegisterUserAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    