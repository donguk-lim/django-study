from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/index.html")

def get_name(request, name):
    context = {}
    context["name"] = name
    return render(request, "pages/name.html", context=context)