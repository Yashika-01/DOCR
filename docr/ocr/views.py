from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from ocr.models import Image
from django.contrib.auth import get_user_model
from .forms import ImageForm
import os
from django.views.decorators.csrf import csrf_exempt

# from django_email_verification import sendConfirm

# Create your views here.
 
def index(request):
      return render(request, 'index.html')

def sign(request):
      return render(request, 'sign.html')

# def register(request):
#       if request.method == 'POST':
#             username = request.POST['username']
#             email = request.POST['email']
#             password= request.POST['password']
#             user = User.objects.create_user(username = username , email = email,  password = password)
#             user.save()
#             print('user created')
#             return redirect('/')
#       else:
#             return render(request,'register.html')

# def sendEmail(request):
#       password = request.post.get('password')
#       username = request.post.get('username')
#       email = request.post.get('email')
#       user = get_user_model().objects.create(username = username, password = password, email = email)
#       sendConfirm(user)
#       return render(request, 'confirm_template.html')


def success(request):
      return render(request, 'success.html')

@csrf_exempt
def digitize(request):
      if request.method== 'POST':
            # uname = request.POST['user']
            # path = f'media/img/{uname}'
            # print(path)
            # if os.path.isdir(path):
            #       print('true')
            # else:
            #       print('false')
            #       os.mkdir(path)
            form = ImageForm(request.POST, request.FILES)   
            if form.is_valid():
                  form.save()
                  # photo = Image.objects.create()
                  # image_file = request.FILES['image']
                  # photo.image.save(path, image_file)
            form = ImageForm()
            img = Image.objects.all()
            return render(request, 'digitize.html',{'img': img, 'form': form})
      form = ImageForm()
      return render(request, 'digitize.html',{'form': form})

def plagiarism(request):
      pass