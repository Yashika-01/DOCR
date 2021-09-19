from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def index(request):
      return HttpResponse("<h1>Welcome to Docr</h1>")

def home(request):
      return HttpResponse("<h1>Homepage</h1>")