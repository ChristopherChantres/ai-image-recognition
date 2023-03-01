from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context = {
    'name': 'Anonymous',
  }

  return render(request, 'index.html', context)


# gets the ulr image from the input and passes to the analyze.html file
def analyze(request):
  context = {
    'user_url': request.GET['userUrlPhoto']
  }
  
  return render(request, 'analyze.html', context)