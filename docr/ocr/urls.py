from django.urls import path
from django.urls.conf import include, include
from . import views
# from django_email_verification import urls as mail_urls

urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.success, name='success'),
    path('digitize', views.digitize, name='digitize')
    # path('email', include(mail_urls))

]
