from django.shortcuts import render
from collections import defaultdict

# Create your views here.
def throw(request):
    return render(request, "pages/throw.html")

def catch(request):
    name = request.POST.get("name")
    if not name:
        pass
    hobby = request.POST.get("hobby")
    if not hobby:
        pass
    context = {}
    context["name"] = name
    context["hobby"] = hobby
    return render(request, "pages/catch.html", context=context)
