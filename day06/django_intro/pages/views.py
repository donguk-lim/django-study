from django.shortcuts import render
from collections import defaultdict

# Create your views here.
def index(request):
    return render(request, "pages/index.html")

def page1(request):
    return render(request, "pages/page1.html")