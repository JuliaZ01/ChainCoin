from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index/index.html')

def aboutus(request):
    return render(request, 'index/aboutus.html')