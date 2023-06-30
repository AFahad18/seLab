from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post, Hotel
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    Context = {
        'posts' : Post.objects.all(),
        'hotels' : Hotel.objects.all(),
    }
    return render(request, 'html/home.html', Context)

def weatehrInfo(request):
    return render(request, 'html/weatherInfo.html')

def blog(request):
    Context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'html/blog.html', Context)

def autoCompleteHotelSearch(request):
    if 'term' in request.GET:
        hotels = Hotel.objects.filter(location__istartswith=request.GET.get('term'))
        locations = list()
        for hotel in hotels:
            locations.append(hotel.location)
        return JsonResponse(locations, safe=False)
    else:
        return redirect(home)