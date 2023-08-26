from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post, Hotel
# from t_logsign.models import Guide
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
            
        uniqueLocations = list(set(locations))
        return JsonResponse(uniqueLocations, safe=False)
    else:
        return redirect(home)
    

def viewHotel(request):
    Context = {
        'hotels' : Hotel.objects.all()
    }
    return render(request, 'html/viewHotel.html', Context)

def searchHotel(request):
    if 'location' in request.GET:
        Context = {
            'hotels' : Hotel.objects.filter(location__istartswith=request.GET.get('location')),
            'location' : request.GET.get('location')
        }        
        return render(request, 'html/hotelSearch.html', Context)
    else:
        return redirect(viewHotel)

def hotelDetails(request, id):
    if id:
        Context = {
            'hotel' : Hotel.objects.get(id = id)
        }
        return render(request, 'html/hotelDetails.html', Context)
    else:
        return render(viewHotel)
    

# def chat(request):
#     return render(request, 'html/chat.html')


# def search_results(request):
#     location = request.GET.get('location')
    
#     if location:
#         guides = Guide.objects.filter(location__icontains=location)
#     else:
#         guides = Guide.objects.none()
    
#     context = {'guides': guides}
#     return render(request, 'html/results.html', context)
