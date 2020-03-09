from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticles


# def home(request):
#     return HttpResponse('Hello World')

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})
