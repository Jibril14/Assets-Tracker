from django.shortcuts import render
from .models import Staff, Employee
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError

from .models import User
from .serializers import UserSerializer
# Create your views here.


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
            username = request.data.get("username")
            email = request.data.get("email")
            password = request.data.get("password")
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
                    role=role)
                user.save()
            else:
                user = Employee.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password)
                user.save()

            serializer = UserSerializer(user)
            return Response(serializer.data)


class LoginUserApiView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.filter(email=email).first()
        if user is None:
            return Response(
                {"error": "No User With this email"},
                status.HTTP_400_BAD_REQUEST,
            )
        if not user.check_password(password):
            return Response(
                {"error": "Wrong Password"},
                status.HTTP_400_BAD_REQUEST,
            )
        serializer = UserSerializer(user)
        return Response(serializer.data)
