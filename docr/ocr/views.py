from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from ocr.models import user_info, Image
from django.contrib.auth import get_user_model
from .forms import ImageForm

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

def digitize(request):
      if request.method== 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
      form = ImageForm()
      img = Image.objects.all()
      return render(request, 'digitize.html', {'img':img,'form':form})