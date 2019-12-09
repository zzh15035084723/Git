from django.shortcuts import render

# Create your views here.


def link(request):
    return render(request,'链接.html')


def index(request):
    return render(request,'index.html')