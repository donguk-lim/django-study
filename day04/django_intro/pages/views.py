from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    menus = ["짜장면", "돈까스", "삼겹살", "햄버거"]
    my_sentence = "Life is short, you need python."
    messages = ["apple", "banana", "cucumber", "mango"]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        "menus": menus,
        "my_sentence": my_sentence,
        "messages": messages,
        "datetimenow": datetimenow,
        "empty_list": empty_list,
    }
    return render(request, "pages/index.html", context=context)

def palindrome(request, pal):
    is_palindrome = True
    for i in range(0, len(pal)//2):
        if pal[i] != pal[len(pal)-i-1]:
            is_palindrome = False
            break

    context = {"is_palindrome": is_palindrome}

    return render(request, "pages/palindrome.html", context=context)