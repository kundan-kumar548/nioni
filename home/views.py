from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages,auth
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    return render(request, 'home/home.html')