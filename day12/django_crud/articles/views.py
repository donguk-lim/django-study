from django.shortcuts import render, redirect
from .models import Article, Comment

# Create your views here.
def index(request):
    context = {}
    articles = Article.objects.all()
    context["articles"] = articles
    return render(request, "articles/index.html", context)

def create(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()

        return redirect("articles:index")
    else:
        return render(request, "articles/create.html")

def read(request, article_id):
    context = {}
    article = Article.objects.get(pk=article_id)
    context["article"] = article
    return render(request, "articles/read.html", context=context)

def update(request, article_id):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        article = Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()

        return redirect("articles:index")
    else:
        context = {}
        article = Article.objects.get(pk=article_id)
        context["article"] = article
        return render(request, "articles/update.html", context=context)

def delete(request, article_id):
    if request.method == "GET":
        article = Article.objects.get(pk=article_id)
        article.delete()
    
    return redirect("articles:index")

def comment_create(request, article_id):
    if request.method == "POST":
        content = request.POST.get("content")
        comment = Comment()
        comment.article = Article.objects.get(pk=article_id)
        comment.content = content
        comment.save()
    return redirect("articles:read", article_id)

def comment_update(request, article_id, comment_id):
    if request.method == "POST":
        content = request.POST.get("content")
        comment = Comment.objects.get(pk=comment_id)
        comment.content = content
        comment.save()
    return redirect("articles:read", article_id)

def comment_delete(request, article_id, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
    return redirect("articles:read", article_id)