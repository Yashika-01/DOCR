from django.contrib import admin
from .models import user_info, Image
# Register your models here.

admin.site.register(user_info)
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
  list_display = ['id', 'photo', 'date']