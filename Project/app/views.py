
from re import L
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .lib import check_existence, create_new_user
from .models import *


class Login(APIView):        
    def post(self, request):
        """
            for authenticating a user
        """ 
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        print(username, password)
        has_username = check_existence(username)
        has_password = check_existence(password)

        if not has_username or not has_password:
            return JsonResponse({
                "message" : "Please provide both username and password"
            })
        print("up", username, password)
        user = authenticate(request, username=username, password=password)
        print("tjis is the user", user)
        if not user:
            return JsonResponse({
                "error" : "Incorrect username or password" 
            })
        token, _ = Token.objects.get_or_create(user=user)

        return JsonResponse({
            "message" : "Login Successful",
            "token": token.key,
            "username": user.username
        })

class User(APIView):
    
    def post(self, request):
        """
            create a new user
        """
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        has_username = check_existence(username)
        has_password = check_existence(password)

        if not has_username or not has_password:
            return JsonResponse({
                "message" : "Please provide both username and password"
            })

        # create new user
        user = create_new_user(username, password)

        print(user.username, password, user.password)

        return JsonResponse({
            "message" : "User Created Successfully"
        })

class Validator(APIView):

    def post(self, request):
        print(request.body)
        file = request.POST.get("file", None)
        user = request.POST.get("username", None)

        print("file", file, "user", user)

        return JsonResponse({
            "message": "hello"
        })