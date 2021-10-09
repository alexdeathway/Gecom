from django.shortcuts import render

from django.http import HttpResponse 

# Create your views here.

def component(request):
    return HttpResponse("this is component")