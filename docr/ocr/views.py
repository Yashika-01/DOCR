from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.http import FileResponse
from django.contrib.auth.models import User, auth
from ocr.models import Image
from django.contrib.auth import get_user_model
from .forms import ImageForm
import os
from django.views.decorators.csrf import csrf_exempt
from fpdf import FPDF
import glob

from django.db import models
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

def makepdf(request):
      from PIL import Image
      pdf = FPDF()
      sdir = "media/img/"
      w, h = 0,0

      files = glob.glob("media/img/*")
      filecount = len(files)
      for i in range(1, filecount+1):
            fname = sdir + "img%.d.jpg" %i
            if os.path.exists(fname):
                  if i ==1:
                        page = Image.open(fname)
                        w, h = page.size
                        pdf = FPDF(unit='pt', format=[w,h])
                  image = fname
                  pdf.add_page()
                  pdf.image(image, 0, 0, w, h)
            else:
                  print('File not found: ', fname)
                  print('Processed %d' % i)

      pdf.output('media/img/Converted_pdf.pdf', "F")
      print('successfully converted ')
      path = "media/img/Converted_pdf.pdf"
      messages.info(request, 'PDF converted succesfully..')
      return FileResponse(open(path, 'rb'), content_type='application/pdf')











def plagiarism(request):
      pass