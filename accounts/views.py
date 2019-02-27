from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages,auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import *
from django.http import *
from .forms import *
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage

# Create your views here.


def login(request):
    if request.method == "POST":
        # user,pas is the name on the input tag of login.html
        username = request.POST['user']
        password = request.POST['pas']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # return render(request, 'wing/welcome.html')
                return redirect('home:home')
            else:
                messages.error(request, "Username and password did not match")
        except ObjectDoesNotExist:
            print("Invalid user")
    return render(request, "accounts/login.html")


def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user1 = authenticate(username=username, password=raw_password)
            request.user = user1
            # home(request)
            # messages.success(request, 'Account created successfully')
            return redirect('accounts:login')
    else:
        form = Signup()
    return render(request, 'accounts/signup.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('home:home')

