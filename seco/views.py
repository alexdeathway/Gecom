from django.shortcuts import render

def index(request):
    return render("index.html")