from django.shortcuts import render
from django.http import HttpResponse

posts=[{
    'content': 'VAAADDDERRRR',
    'title': 'POST1',
    'author': 'Mike',
    'date_posted': 'November 6 2018',
    },
    {
    'content': 'ATSTS',
    'title': 'POST2',
    'author': 'Rich',
    'date_posted': 'November 7 2018',
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'about'})
# Create your views here.

def abouter(request):
    return HttpResponse('<h2><font color = "red"> THIS IS ABOUTER </font></h2>')