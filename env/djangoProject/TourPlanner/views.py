from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from .models import Post
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    return render(request, 'html/home.html')

def weatehrInfo(request):
    return render(request, 'html/weatherInfo.html')