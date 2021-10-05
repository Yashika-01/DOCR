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
from ocr.vision import gcs

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

      files = []
      files = glob.glob("media/img/*")
      print(files)
      files.sort()
      print(files)
      filecount = len(files)
      for i in range(0, filecount):
            c = files[i]
            a,b,c = c.split('/')
            fname = sdir + c
            print(fname)
            if os.path.exists(fname):
                  if i == 0:
                        page = Image.open(fname)
                        w, h = page.size
                        pdf = FPDF(unit='pt', format=[w,h])
                  image = fname
                  pdf.add_page()
                  pdf.image(image, 0, 0, w, h)
            else:
                  print('File not found: ', fname)
                  print('Processed %d' % i)

      

      # pdf.output('media/img/Converted_pdf.pdf', "F")
      pdf.output('/home/neha/Downloads/Converted_pdf.pdf', "F")
      print('successfully converted ')
      res = clean()
      if res == 'done':
            print('images deleted successfully..')
      # path = "media/img/Converted_pdf.pdf"
      path = "/home/neha/Downloads/Converted_pdf.pdf"
      
      return FileResponse(open(path, 'rb'), content_type='application/pdf')


def clean():
      path = f'media/img/'
      if os.listdir(path) == []:
            print('No images found')
      else:
            print('images found')
            files = glob.glob('media/img/.jpg')
            for f in files:
                  print(f)
                  os.remove(f)
            Image.objects.all().delete()
      return 'done'



def plagiarism(request):
      pass


def vision(request):
      # files = []
      # files = glob.glob("media/img/*")
      # print(files)
      # files.sort()
      # print(files)

      # filecount = len(files)
      # r = 'Extracted text: \n'
      # for i in range(0, filecount):
      #       resp = vision()
      #       r = r + resp
      #       i = i +1
      if request.method == 'POST':
            print('hello')
            sdir = "media/img/"
            files = []
            files = glob.glob("media/img/*")
            print(files)
            files.sort()
            print(files)
            filecount = len(files)
            r = 'Extracted text: \n'
            for i in range(0, filecount):
                  c = files[i]
                  a,b,c = c.split('/')
                  fname = sdir + c
                  print(fname)
                  if os.path.exists(fname):
                        # if i == 0:
                        #       page = Image.open(fname)
                        #       w, h = page.size
                        #       pdf = FPDF(unit='pt', format=[w,h])
                        resp = gcs(fname)
                        r = r + resp
                  else:
                        print('File not found: ', fname)
                        print('Processed %d' % i)
            print(r)
            var = r
            return render(request, 'success.html', {'container': var} )


def sleepy(request):
      var = 'I is very sleepy'
      return render(request, 'success.html', )