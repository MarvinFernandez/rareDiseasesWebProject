from django.shortcuts import render
from news.models import Post, Category

# Create your views here.


def News(request):

    posts=Post.objects.all()
    return render(request, "news/news.html", {"posts": posts})

def CategoryView(request, category_id):

    category=Category.objects.get(id=category_id)
    posts=Post.objects.filter(categories=category)
    return render(request, "news/categories.html", {"category": category, "posts": posts})