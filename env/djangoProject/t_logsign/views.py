from django.shortcuts import render,HttpResponse,redirect
from .models import Guide
# Create your views here.
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
            return redirect('html/home.html')
    return render (request, 'html/signup.html')

def LoginPage(request):
    return render (request, 'html/login.html')

