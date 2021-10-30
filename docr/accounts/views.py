from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ocr.models import Image
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
import os
import glob
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import random, math
from django.http import JsonResponse
# Create your views here.


vcode = random.randint(1000, 9999)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # print('Username already exists.')
                messages.error(request, 'Username taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username , email = email,  password = password1)
                user.save()
                request.session['og_code'] = vcode
                send_mail('Welcome to  DOCR', f'thank you for registering with DOCR. Your verification code is {vcode}', 'docr.ocr@gmail.com', [email], fail_silently=False)
                # return render(request, 'email_verify.html', {'email': email, 'vcode': vcode})
                return redirect('email_verify')
        else:
            messages.error(request, 'Password mismatch')
            return redirect('register')
        
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            request.session['username'] = username
            print('Your name is: ' ,request.session.get('username'))
            return render(request, 'services.html', {'username': username})
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('register')

    else:
        return render(request, 'register')



def logout(request):
    path = f'media/img/'
    if os.listdir(path) == []:
        print('No images found')
    else:
        print('images found')
        files = glob.glob('media/img/*')
        for f in files:
            print(f)
            os.remove(f)
        Image.objects.all().delete()
    request.session.clear()
    print('deleted session')
    messages.info(request, 'Adios!, hope to see you soon buddy...')
    print('Adios!, hope to see you soon buddy...')
    return render(request, 'index.html')



def email_verify(request):
    vcode = request.session['og_code']
    print(vcode)
    if request.method == "POST":
        user_code = request.POST['code_field']
        if(int(user_code) == int(vcode)):
            print('OTP verified')
            messages.success(request, 'OTP verified')
            messages.success(request, 'Account registered successfully!')
            messages.info(request, 'Login to avail the services')
            return render(request, 'register.html')
        else:
            print('OTP incorrect')
            messages.error(request, 'Incorrect OTP')
            return render(request, 'email_verify.html')

    return render(request, 'email_verify.html')