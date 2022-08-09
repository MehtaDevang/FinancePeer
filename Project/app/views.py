
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.views import APIView

from .lib import check_existence, create_new_user
from .models import *
class Login(APIView):        
    def post(self, request):
        """
            for authenticating a user
        """ 
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        has_username = check_existence(username)
        has_password = check_existence(password)

        if not has_username or not has_password:
            return JsonResponse({
                "message" : "Please provide both username and password"
            })
        print("up", username, password)
        user = authenticate(request, username=username, password=password)
        print("tjis is the user", user)
        return JsonResponse({
            "message" : "Login API"
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