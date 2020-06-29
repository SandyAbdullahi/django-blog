from django.shortcuts import render, redirect

from . import models
from .forms import CreatePostForm

def home(request):
    posts = models.Post.objects.all()
    title = 'I am Kek'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'pages/home.html', context)

def new_post(request):
    new_post_form = CreatePostForm()
    if request.method == 'POST':
        new_post_form = CreatePostForm(request.POST, request.FILES)
        if new_post_form.is_valid():
            new_post_form.save()
            return redirect('home')
        else:
            return render(request, 'error/wrong-form.html')
    else:
        context = {
            'form':new_post_form
        }
    return render(request, 'forms/new_post.html', context)

def about(request):
    return render(request, 'pages/about.html')