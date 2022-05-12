from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')

def category(request):
    return render(request, 'blog/category.html')
