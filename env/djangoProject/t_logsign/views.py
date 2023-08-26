from django.shortcuts import render,HttpResponse,redirect
from .models import Guide
# Create your views here.

def authenticate_guide(username, password):
    try:
        guide = Guide.objects.get(name=username)
        if guide.password == password:
            return guide
    except Guide.DoesNotExist:
        return None


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        location=request.POST.get('location')
        number=request.POST.get('number')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Password and Confirmed Password are not same")
        else:
            my_user = Guide.objects.create(name=uname, email=email, location=location, number=number, password=pass1)
            my_user.save()
            # return HttpResponse("User has been created Successfully")
            # print(uname,email,location,number,pass1,pass2)
            return redirect('/')
    return render (request, 'html/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate_guide(username, pass1)
        print(user)
        if user is not None:
            return redirect('/')
        else:
            return HttpResponse("Username and Password is incorrect!!!")
    return render (request, 'html/login.html')

