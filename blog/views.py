from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'about'})
# Create your views here.

def abouter(request):
    return HttpResponse('<h2><font color = "red"> THIS IS ABOUTER </font></h2>')