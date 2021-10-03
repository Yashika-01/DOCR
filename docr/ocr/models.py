from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.
class user_info(models.Model):
    name = models.CharField(max_length = 1000, default="")
    email= models.CharField(max_length=1000, default="")
    password = models.CharField(max_length=1000, default="")


class Image(models.Model):
    photo = models.ImageField(upload_to = f"img/")
    date = models.DateTimeField(auto_now_add=True)