from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
    if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password= request.POST['password']
            user = User.objects.create_user(username = username , email = email,  password = password)
            user.save()
            print('user created')
            return redirect('/success')
    else:
            return render(request,'register.html')