from django.db import models

# Create your models here.
class user_info(models.Model):
    name = models.CharField(max_length = 1000)