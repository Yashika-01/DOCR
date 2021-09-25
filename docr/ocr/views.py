from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from ocr.models import user_info

# Create your views here.
 
def index(request):
      return render(request, 'index.html')

def sign(request):
      return render(request, 'sign.html')

def register(request):
      if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password= request.POST['password']
            user = User.objects.create_user(username = username , email = email,  password = password)
            user.save()
            print('user created')
            return redirect('/')
      else:
            return render(request,'register.html')

def success(request):
      return render(request, 'success.html')

