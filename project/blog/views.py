from django.shortcuts import render

def home(request):
    title = 'I am Kek'
    context = {
        'title': title,
    }
    return render(request, 'pages/home.html', context)