from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
# Create your views here.

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
                messages.success(request, 'Account registered successfully!')
                messages.info(request, 'Login to avail the services')
                return redirect('register')
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
    request.session.clear()
    print('deleted session')
    return redirect('index')