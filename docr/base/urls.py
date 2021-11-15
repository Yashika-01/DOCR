
from django.urls import path
from .views import sub, success, service
from ocr.views import continued

urlpatterns = [
    path('sub', sub, name='sub'),
     path('success' , success , name='success'),
     path('service', continued, name="service")
]
