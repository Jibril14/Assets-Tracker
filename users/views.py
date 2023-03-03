from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password 
from .models import Staff, Employee
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer


class RegisterUserAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')

        try:
            User.objects.get(email=email, username=username)
            return Response(
                {"error": "This username or email already exist"},
                status=status.HTTP_403_FORBIDDEN,
            )
        except User.DoesNotExist:
            user = User()
            user.set_password(raw_password=request.data.get('password'))
            username = request.data.get("username")
            email = request.data.get("email")
            password = make_password(request.data.get("password"))
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            role = request.data.get("role").lower()

            if role == "staff":
                user = Staff.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                    role=role
                )
                user.save()
                token = Token.objects.create(user=user)
            else:
                user = Employee.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password
                )
                user.save()
                token =Token.objects.create(user=user)
            
            return JsonResponse({"token":str(token)}, status=status.HTTP_201_CREATED)
           


class LoginUserApiView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        #username = User.objects.get(email=email).username

        user = authenticate(request, email=email, password=password)
        if user is not None:
            response = {
                "success": "Login Successfull",
                "token":user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
                  
        else:
            return Response(
                {"error": "Invalid email or password"},
                status.HTTP_400_BAD_REQUEST,
            )
    
    def get(self, request):
        content = {
            "user": str(request.user),
            "token": str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)