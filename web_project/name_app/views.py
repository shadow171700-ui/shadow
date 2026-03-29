from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hallo(request):
  return HttpResponse("Hello shadow how are you!")


