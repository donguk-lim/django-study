from django.shortcuts import render, redirect
from .models import Article

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