from django.shortcuts import render, HttpResponse

# Create your views here.
 
def index(request):
      return render(request, 'index.html')

def home(request):
      return HttpResponse("<h1>Homepage</h1>")
