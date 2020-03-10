from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticles


# def home(request):
#     return HttpResponse('Hello World')

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})

def blog_article(request, article_id):
    article = BlogArticles.objects.get(id=article_id)
    pub = article.publish
    return render(request, 'blog/content.html', {'article': article, 'publish': pub})
