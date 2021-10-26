# day4: DTL(Django Template Language)



## 복습([day3 링크](../day03/README.md))

- get으로 요청하고 받기(query string)



## 오늘 학습 내용

- path parameter 실습: palindrome
- DTL(Django Template Language)



## palindrome 

앞뒤를 뒤집어도 똑같은 문자열을 palindrome이라고 합니다.

`GET http://localhost:8000/palindrome/<str:pal>`

를 요청했을 때, True / False를 보여주는 페이지를 작성해 주세요.



### 풀이

urls.py, settings.py 는 day2, day3와 동일합니다.

```python
# pages/views.py
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def palindrome(request, pal):
    is_palindrome = True
    for i in range(0, len(pal)//2):
        if pal[i] != pal[len(pal)-i-1]:
            is_palindrome = False
            break

    context = {"is_palindrome": is_palindrome}

    return render(request, "pages/palindrome.html", context=context)
```

```html
<!-- pages/templates/pages/palindrome.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    palindrome: {{is_palindrome}}
</body>
</html>
```





## DTL

장고 프레임워크를 크게 관통하는 디자인 패턴은 MTV(Model Template View) 패턴입니다. 여기에서 View는 MVC 패턴의 컨트롤러와 같은 역할이고, Template으로 계산한 값들을 전달해주는 역할을 합니다.

그리고 Template에서 그 값을 전달 받아서 html파일이 완성이 됩니다.

Template에 값을 집어 넣을 때, 어떻게 집어 넣을 지에 관련된 문법이 DTL입니다.



오늘 사용할 소스코드는 다음과 같습니다.

```python
# django_intro/pages/urls.py

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index),
]
```

```python
# django_intro/pages/views.py

from django.shortcuts import render
from datetime import datetime

def template_language(request):
    menus = ["짜장면", "돈까스", "삼겹살", "볶음밥"]
    my_sentence = "Life is short, you need python."
    messages = ["apple", "banana", "cucumber", "mango"]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        "menus": menus,
        "my_sentence": my_sentence,
        "datetimenow": datetimenow,
        "empty_list": empty_list,
        "messages": messages
    }
    return render(request, "pages/template_language.html", context)
```

```html
<!-- django_intro/pages/templates/pages/template_language.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h3>1. 반복문</h3>
    {% for menu in menus %}
    <p>{{forloop.counter}} {{menu}}</p>
    <!-- forloop.counter를 넣으면 몇 번째 돌고 있는지 셀 수 있음 -->
    {% endfor %}
    
    {% for user in empty_list %}
    <p>{{user}}</p>
    {% empty %}
    <!-- empty: for 태그 안에 optional 하게 있음. 빈 리스트일 때 출력됨 -->
    <p>현재 가입한 유저가 없습니다.</p>
    {% endfor %}
    <hr>

    <h3>2. 조건문</h3>
    {% if "돈까스" in menus %}
    <p>돈까스 JMT</p>
    {% endif %}
    <hr>

    {% for menu in menus %}
        {{forloop.counter}}번째 도는 중..
        {% if forloop.first %}
        <p>짜장면 + 고춧가루</p>
        {% else %}
            <p>{{menu}}</p>
        {% endif %}
    {% endfor %}

    <h3>3. length filter 활용</h3>
    {% for message in messages %}
    <!-- filter | -->
      {% if message|length > 5 %}
      <p>{{message}}, 글자가 너무 길어요.</p>
      {% else %}
      <p>{{message }}, {{message|length}}</p>
      {% endif %}
    {% endfor %}
    <hr><hr>

    <h3>4. lorem ipsum</h3>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum vero quibusdam voluptates officiis a harum corporis deleniti, veritatis impedit iure in, hic amet eaque, placeat molestias eligendi dolorum facilis fugit.
    <hr>
    <!-- 3개의 word를 뽑아줌 -->
    {% lorem 3 w %}
    <!-- 2개의 paragraph를 뽑아줌 -->
    {% lorem 2 p %}

    <h3>5. 글자수 제한(truncate)</h3>
    <!-- 단어 단위로 자르기 -->
    <p>{{my_sentence|truncatewords:3}}</p>
    <!-- 문자 단위로 자르기 -->
    <p>{{my_sentence|truncatechars:3}}</p>

    <h3>6. 글자 관련 필터</h3>
    <p>{{'abc'|length}}</p>
    <p>{{'ABC'|lower}}</p>
    <!-- 각 단어의 첫 번째 문자만 대문자로 나옴 -->
    <p>{{my_sentence|title}}</p>
    <!-- 첫 번째 문자만 대문자로 나옴 -->
    <p>{{'abc def'|capfirst}}</p>
    <!-- 하나만 랜덤으로 뽑아서 반환함 -->
    <p>{{menus|random}}</p>

    <h3>7. 연산</h3>
    <!-- 연산은 파이썬에서 처리하는게 낫기 때문에 사용할 일이 없습니다. -->
    <p>{{ 4|add:6}}</p>
    <hr>

    <h3>8. 날짜 표현</h3>
    {{ datetimenow }}<br>
    <!-- 같은 날짜표현이지만 now는 장고에서 제공해주는 기능입니다, -->
    {% now 'DATETIME_FORMAT'%}<br>
    {% now 'SHORT_DATETIME_FORMAT'%}<br>
    {% now 'DATE_FORMAT'%}<br>
    {% now 'SHORT_DATE_FORMAT'%}<br>

    <h3>9. 기타</h3>
    {{ 'google.com'| urlize }}


</body>
</html>
```





## 다음 시간 배울 내용

- post로 값 받기
- bootstrap
- template 상속

