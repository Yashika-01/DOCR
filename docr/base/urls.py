
from django.urls import path
from .views import sub, success

urlpatterns = [
    path('sub', sub, name='sub'),
     path('success' , success , name='success')
]
