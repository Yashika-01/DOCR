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

string=""
op=[]
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
      pdf.output('/home/yashika/Downloads/Converted_pdf.pdf', "F")
      print('successfully converted ')
      res = clean()
      if res == 'done':
            print('images deleted successfully..')
      # path = "media/img/Converted_pdf.pdf"
      path = "/home/yashika/Downloads/Converted_pdf.pdf"
      
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
            r = ''
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
            var=str(r)
            global string 
            string = var
            return render(request, 'done1.html')


def sleepy(request):
      global string
      var=string
      print(var)
      #var = 'Extracted text: \nRemember that texture plays an important part in\nthe beauty of crochet. The finer mercerised threads\nare more effective for the delicate designs used for\ntablecloths, doilies, edgings and accessories, while\nthe heavier threads are used for bedspreads,\nchairbacks, luncheon mats, etc. Crochet hooks\nare made of steel, composition or bone. Steel\ncrochet hooks range in size from number 310,\nthe largest, to number 8, the smallest.\n" } We know from the diaries of Samuel Pepys\nthat he was a\ngreat man for lace\npaying\nas much as 3 for a lace collar. But this\ndidn\'t mean he was prepared to do as much\nfor his lady, for he records testily: \'My wife\nand I fell out about\nmy\nnot being willing\nto have her gown laced.\'\n" }'
      files = []
      files = glob.glob("media/img/*")
      files.sort()
      filecount = len(files)
      if filecount==1:
            sent=[]
            final_sent=[]
            var=var.replace("}"," ")
            var=var.replace('"','"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
            sent = var.split(sep='\\n')
            final_sent = final_sent + sent
      else:
            paras=[]
            paras = var.split("}",(filecount-1))
            sent=[]
            final_sent=[]
            for para in paras:
                  para=str(para)
                  para=para.replace("}"," ")
                  para=para.replace('"','"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
                  sent = para.split('\\n')
                  final_sent = final_sent + sent
      var=final_sent
      global op 
      op = var
      return render(request, 'success.html',{'container':var} )

def saving(request):
      global op
      print(string)
      with open('/home/yashika/Downloads/extracted_text.txt', 'w') as f:
            for ops in op:
                  f.write(ops)
                  f.write('\n')
      return render(request, 'done.html')

def continued(request):
      return render(request,'services.html')