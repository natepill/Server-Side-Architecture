from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author': 'Nathan',
    'title': 'This is my title!'
    },
    {
    'author': 'Joe',
    'title': 'HI!'
    }
]


# Logic for where we handle where we send users based on routing

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'ABOUt'})
