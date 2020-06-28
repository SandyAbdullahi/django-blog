from django.shortcuts import render

from . import models

def home(request):
    posts = models.Post.objects.all()
    title = 'I am Kek'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'pages/home.html', context)