## 복습([day 1 링크](../day01/README.md))

- 이론
  - MTV Pattern(model, view, template)
- 실습
  - venv 가상 환경 생성
  - project 생성(django-admin startproject <proj_name>)
  - app 생성(django-admin startapp <app_name>)
  - template, view를 사용한 첫 페이지 띄우기

## 오늘 학습 내용

- 이론
  - 다른 페이지로 인자 전달 방법 소개
    - get: path parameter, query string
    - post: request body

- 실습
  - path parameter 실습(restful한 형태)
- 기타
  - emmet 소개



## parameter를 전달 받는 방법

> get, post 처럼 html의 전달에 관한 약속들을 http(hyper text transfer protocol)이라고 부르고,
> http method에는 get, post, put, fetch, options 등의 method들이 있습니다.
> get method는 html을 클라이언트 pc의 브라우저가 획득하기 위해서 사용되고,
> post method는 server에 정보를 전달하기 위해서 사용됩니다.

- get
  - path parameter: `http://abc.com/posts/123/comments/3` 이런식으로 post의 id, comment의 id를 url 경로에 포함해서 변수 값을 전달하는 방식입니다.
  - query string: `http://abc.com?board_id=abab&page=3` 의 예제처럼, 주소창에서 key, value들을 &로 묶어서 서버에 변수 값을 전달하는 방식입니다.

- post
  - request body



오늘 GET으로 인자를 넘겨 받은 부분은 `path parameter` 방식으로 진행하겠습니다.

## 실습(GET method: path parameter로 받기)

주소창에서  `<str:name>/`으로 이름 전달 받아서, 이름 출력




```
# django_intro/pages/urls.py

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('<str:name>/', views.introduce), # <타입:이름> 형식으로 path parameter 받음
    # path('persons/<str:name>/birth/<str:birth>/') 이런식으로 여러 개 인자를 전달할 수도 있습니다.
]
```
```
# 뷰: django_intro/pages/views.py
# context에 dictionary형식으로 넣어줍니다.
# views에서 request 이후에 인자로 받습니다.

from django.shortcuts import render

def introduce(request, name):
    context = {'name': name}
    return render(request, 'pages/name.html', context)
```
```
<!-- 템플릿: django_intro/pages/templates/pages/name.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <p>
        안녕하세요 {{name}}입니다😄.
    </p>
    <p>
        제 생일은 {{birth_month}}월에 있습니다!
    </p>
</body>
</html>
```

아래와 같은 주소로 접근하면, 결과가 나오는 것을 볼 수 있습니다.

> TIP: html 파일 내에서는 emmet을 사용할 수 있습니다. emmet은 입력에 대해서 자동완성을 해주는 기능입니다.
>
> 예) p + tab => p tag 생성, p*2 + tab => p tag 2개 생성 등. 앞으로 많이 사용할 기능이라서, 필요한 기능이 생길 때마다 말씀 드리겠습니다.
> css selector에 대해서 좀 더 자세히 알게 되면, emmet을 좀 더 편하게 쓸 수 있습니다.



## 다음 시간 내용

템플릿 파일(html 파일) 에서는 DTL(Django)을 사용해서 반복문과 제어문 등을 사용할 수 있습니다. DTL에 대해서 알아보겠습니다.