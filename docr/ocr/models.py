from django.db import models

# Create your models here.
class user_info(models.Model):
    name = models.CharField(max_length = 1000, default="")
    email= models.CharField(max_length=1000, default="")
    password = models.CharField(max_length=1000, default="")