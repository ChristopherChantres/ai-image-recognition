from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
  context = {
    'name': 'Anonymous',
  }

  return render(request, 'index.html', context)


# gets the ulr image from the input and passes to the analyze.html file
def analyze(request):
  # user_url =  request.GET['userUrlPhoto']
  # api_key = 'acc_18c42d78bf628e4'
  # api_secret = '20f06b8787e07e922f0a1a2c154fbb39'
  
  # # make the HTTP request payload with the image URL
  # response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % user_url, auth=(api_key, api_secret))
  # response_dictionary = response.json()
  # trusty_results = []
  # counter = 1

  # # validate if the request is succeding or failing
  # if response.status_code == 200:
  #   print('It is working!:\n')
  # else:
  #   print(f'The status code is: {response.status_code}')
  
  # # iterate each item inside of {'result:' {'tag': ...}} and validate their confidence > 30
  # # add those items to trusty_results dictionary
  # for item in response_dictionary["result"]["tags"]:
  #   if item["confidence"] > 50:
  #     trusty_results.append(item)

  # # iterate each item of trusty_results and print its name and confidence
  # for feature in trusty_results:
  #   print(f'({counter}) {feature["tag"]["en"].upper()} with {round(feature["confidence"], 2)}% confidence')
  #   counter = counter + 1


#-----------------------------------------------------#
  # list for testing to avoid the use of the API
  trusty_results = [{'confidence': 69.5724258422852, 'tag': {'en': 'tree'}}, {'confidence': 61.9523582458496, 'tag': {'en': 'lakeside'}}, {'confidence': 61.5426292419434, 'tag': {'en': 'shore'}}, {'confidence': 58.9639549255371, 'tag': {'en': 'landscape'}}, {'confidence': 55.575325012207, 'tag': {'en': 'water'}}, {'confidence': 69.5724258422852, 'tag': {'en': 'tree'}}, {'confidence': 61.9523582458496, 'tag': {'en': 'lakeside'}}, {'confidence': 61.5426292419434, 'tag': {'en': 'shore'}}, {'confidence': 58.9639549255371, 'tag': {'en': 'landscape'}}, {'confidence': 55.575325012207, 'tag': {'en': 'water'}}]

  context = {
    'user_url': request.GET['userUrlPhoto'],
    'trusty_results': trusty_results
  }
  
  return render(request, 'analyze.html', context)