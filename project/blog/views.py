from django.shortcuts import render, redirect


from . import models
from .forms import CreatePostForm

def home(request):
    posts = models.Post.objects.all()
    title = 'Welcome to Ab Log'
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

def post_view(request, post_id):
    posts = models.Post.objects.get(pk=post_id)
    context = {
        'post': posts
    }
    return render(request, 'pages/post_detail.html', context)


def update_post(request, post_id):
    p_id = int(post_id)
    try:
        selected_post = models.Post.objects.get(id = p_id)
    except models.Post.DoesNotExist:
        return redirect('home')
    post_form = CreatePostForm(request.POST or None, instance=selected_post)
    if post_form.is_valid():
        post_form.save()
        return redirect('home')
    context = {
            'form':post_form
    }
    print(request)
    return render(request, 'forms/update_post.html', context)

def delete_post(request, post_id):
    p_id = int(post_id)
    try:
        selected_post = models.Post.objects.get(id = p_id)
    except models.Post.DoesNotExist:
        return redirect('home')
    selected_post.delete()
    return redirect('home')


def about(request):
    return render(request, 'pages/about.html')


def why_django(request):
    return render(request, 'pages/static_pages/why_django.html')




# ERROR PAGES

def error404(request):
    return render(request, 'error/page_not_found.html')