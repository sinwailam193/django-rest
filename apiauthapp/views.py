from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer
from utils import const


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token = serializer.save()
            userDict = serializer.data
            data = {
                "user": {"email": userDict["email"], "username": userDict["username"]},
                "token": token,
            }
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(
            const.INTERNAL_SERVER_ERROR_MSG,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class LoginView(APIView):
    def post(self, request):
        return Response("success log in", status=status.HTTP_200_OK)


class TestView(APIView):
    def get(self, request):
        return Response("success test", status=status.HTTP_200_OK)


class LogoutView(APIView):
    def delete(self, request):
        return Response("success log out", status=status.HTTP_200_OK)
