from django.shortcuts import render

def credits_view(request):
    return render(request, 'home/credits.html')

def about_view(request):
    return render(request, 'home/about.html')
