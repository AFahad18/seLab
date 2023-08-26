from django.urls import path
from . import views
app_name = 't_logsign'
urlpatterns = [
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
     path('search/', views.search, name='search'),  # New view for the search form
    path('search_results/', views.search_results, name='search_results'),
    # path('send', views.send, name='send'),
    # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]