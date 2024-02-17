from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def home(request):
    post = Blog.objects.all()
    return render(request, 'index.html', {"post":post})

def add(request):
    return render(request, 'add.html')

