from django.urls import path
from django.urls.conf import include, include
from . import views
# from django_email_verification import urls as mail_urls

urlpatterns = [
    path('', views.index, name='index'),
    # path('sessions', views.sessions, name='sessions'),
    path('success', views.success, name='success'),
    path('digitize', views.digitize, name='digitize'),
    path('plagiarism', views.plagiarism, name='plagiarism'),
    path('makepdf', views.makepdf, name='makepdf'),
    path('vision', views.vision, name='vision'),
    path('sleepy', views.sleepy, name='sleepy'),


    # path('email', include(mail_urls))

]
