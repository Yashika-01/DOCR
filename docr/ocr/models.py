from django.db import models
from django.contrib.auth.models import User, auth
import datetime
# Create your models here.
class user_info(models.Model):
    name = models.CharField(max_length = 1000, default="")
    email= models.CharField(max_length=1000, default="")
    password = models.CharField(max_length=1000, default="")

def splitname(instance, filename):
    name, ext  = filename.split('.')
    name = 'image' + str(datetime.datetime.now())
    filename = name + '.' + ext
    return 'img/{}'.format(filename) 
class Image(models.Model):
    photo = models.ImageField(upload_to = splitname)
    date = models.DateTimeField(auto_now_add=True)