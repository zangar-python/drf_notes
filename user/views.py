from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializer import RegisterSerializer

class RegisterView(APIView):
    def post(self,request:Request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message":"registered"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request:Request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(request,email=email,password=password)
        if not user:
            return Response({"error":"неверные данные"},status=status.HTTP_400_BAD_REQUEST)
        token,created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key})

class UserDataViews(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request:Request):
        user = request.user
        return Response({
            "email":user.email,
            "password":user.password
        })