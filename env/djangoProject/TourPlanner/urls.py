from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('weatherInfo/', views.weatehrInfo, name='weatherInfo'),
    path('blog/', views.blog, name='blog'),
    path('autoCompleteHotelSrc/', views.autoCompleteHotelSearch, name='autoCompleteHotelSearch'),
    path('searchedHotel/', views.searchedHotel, name='searchedHotel'),
    path('hotels/', views.viewHotel, name="allHotels")

]