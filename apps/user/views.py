from django.shortcuts import render,redirect
from apps.user.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request ):
    return render(request,'index.html', locals())

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email'),
        phone = request.POST.get('phone'),
        password = request.POST.get('password'),
        confirm_password = request.POST.get('confirm_password'),
        if password == confirm_password and username and email and phone:
            user = User.objectss.create_user(username=username, email=email, phone=phone)
            user.phone = phone
            user.save()

            user = authenticate(request=request,username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile', user.id)
    
    return render(request,'register-3.html', locals())


def profile(request, id):
    user = User.objectss.get(id=id)
    return render(request,'profile.html', locals())

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return redirect('login')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            return redirect('login')        
        return render(request,'login.html', locals())