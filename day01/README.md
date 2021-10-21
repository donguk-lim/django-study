# day 01 - django overview



# Django

## history of django

django의 탄생 - 신문사에서 만들어졌음

2005년 7월

2008년 v1.0

2017 v2.0

2019 v3.0 ([release note](https://docs.djangoproject.com/en/3.0/releases/3.0/))

## django의 인기

- 국내 - 국내에서 주류는 아니지만, AI와의 호환성이 좋음(flask도 마찬가지). 파이썬 언어 특성상 다른 언어들보다 처리 속도가 약간 느립니다.
  - java - spring이 대다수
  - nodejs(express), golang 등의

- 해외
  - [https://hotframeworks.com](https://hotframeworks.com/)
  - 글로벌하게는 생각보다 꽤 인기 있음



## 카페를 창업하는 두 가지 방법

- A-Z 전부 스스로 하는 방법
- 프렌차이즈 카페를 여는 방법



## 웹 서비스를 제작하는 두 가지 방법

- A-Z 전부 스스로 하는 방법 - flask(or fastapi)
- 프레임워크를 사용해서 웹 서비스를 제작하는 방법(django)



instagram, nasa, moz://a, youtube가 django를 사용했음

웹 프레임워크들은 대부분 MVC 라는 디자인 패턴을 사용하는데 장고는 MTV(model, template, view)로 구성되어 있습니다.



## 가상환경 만들기

1. git bash와 **visual studio code**가 설치되어 있다고 가정합니다.

> 파이썬 버전은 3.6 이상이 요구됩니다.
> 너무 최신 버전의 python에서는 django가 설치되지 않을 수 있습니다.
> 여러 개의 python을 사용해야 하는 경우라면 pyenv 라이브러리도 고려해 볼 수 있습니다.

```
# root 폴더 생성
$ mkdir django-study && cd django-study
```



1.1. windows의 경우

```
C:\Users\NOTA2001\Desktop\django-study> python -m venv venv
C:\Users\NOTA2001\Desktop\django-study> venv\Scripts\activate.bat
```

1.2. linux or mac의 경우

```
$ python -m venv venv
$ vi ~/.bashrc
# ~/.bashrc 의 가장 아래에 한 줄 추가
alias activate="source venv/Scripts/activate"
# venv directory가 있는 디렉토리에서 아래의 명령 실행
activate
```

위의 내용을 .bashrc에 기록합니다.

(linux only)이후로 django-intro 에서 `activate`를 실행하면 됩니다.

리눅스에서 혹시 선호하시는 가상환경 세팅이 있으시면 그렇게 세팅하셔도 좋습니다. 이후에 영향을 미치는 부분은 아닙니다.

(예를 들어, virtualenv-wrapper를 설치하셔서 workon으로 작업환경 바꾸셔도 상관없습니다.)


1. django 설치 및 실행 해보기

```
# django install
(venv) python -m pip install pip --upgrade
(venv) pip install django

# django 프로젝트 만들기
(venv) django-admin startproject proj1
# (venv) django-admin startproject django_intro . # 만약 새 폴더를 만들지 않고, 장고 프로젝트를 시작하려면 .을 붙이면 됨

# 서버 실행
(venv) python manage.py runserver
# 만약 8000번 포트를 사용하고 있는 경우라면, python manage.py runserver 0.0.0.0:8002 로 포트를 바꿔서 실행
# 공인IP를 사용하고 있는 서버의 경우 python manage.py runserver 0.0.0.0:8000 등의 명령어로 외부로 노출시킬 수 있습니다.
# 접속은 http://<서버ip>:8000 으로 접속하시면 됩니다. 단, 사설 ip(192.~, 172.~) 등의 ip 주소로는 바로 접속 되지는 않습니다(힌트: ngrok 사용하면 사설ip라도 가능)
```

> tip 현재까지의 폴더 트리 구조 확인: linux에서의 구조도 동일합니다.
>
> 상위 폴더인 django-study는 다른 것으로 지으셔도 상관없으며, django_intro는 같은 폴더 이름으로 한 번 더 있는 것이 정상입니다.

```
proj1
├── db.sqlite3
├── manage.py
└── proj1
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

[![image-20210521102011969](https://github.com/dwlim-nota/django-study/raw/main/day1/img/1/image-20210521102011969.png)](https://github.com/dwlim-nota/django-study/blob/main/day1/img/1/image-20210521102011969.png)

크롬을 켜고 localhost:8000(혹은 지정한 포트로)으로 들어가면, django 페이지가 마중을 나와줍니다 !!

```
$ python manage.py startapp pages # pages는 앱 이름입니다.
```

> 현재까지의 폴더 구조

```
proj1
├── db.sqlite3
├── manage.py
├── pages
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── proj1
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```



django_admin에는 project에 관한 파일들이 있고, 앱을 만들면 앱에 관한 페이지가 나타납니다.

proj1 밑에 있는 settings.py 파일에서

여기에 INSTALLED_APPS에 'pages'를 한줄 추가해줘야 합니다.

[![image-20210521103336861](https://github.com/dwlim-nota/django-study/raw/main/day1/img/1/image-20210521103336861.png)](https://github.com/dwlim-nota/django-study/blob/main/day1/img/1/image-20210521103336861.png)

[![image-20210521103427149](https://github.com/dwlim-nota/django-study/raw/main/day1/img/1/image-20210521103427149.png)](https://github.com/dwlim-nota/django-study/blob/main/day1/img/1/image-20210521103427149.png)

LANGUAGE_CODE도 en-us에서 ko-kr로 바꿔줍니다.



## urls 작성(router라고도 부름)

proj1/proj1/urls.py

```
"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')), # root url에 연결.
    # 만약 root 주소에 연결하고 싶다면, path('', include('pages.urls')),
]
```



proj1/pages/urls.py

pages 밑에 urls.py 파일을 새로 생성해 준 후에, 다음과 같이 입력해 줍니다.

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
```



## index페이지에 대한 뷰 만들기

proj1/pages/views.py

```
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
```

위와 같이 적을 수 있는데, 장고가 자동으로 templates를 잡기 때문에 pages부터만 적으면 됩니다.



## index 템플릿 만들기

proj1/pages/templates/pages/index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h2>Hi django</h2>
</body>
</html>
```



$ python manage.py runserver


위의 명령어를 실행한 후, index로 접속하면 다음과 같은 창이 뜨게 됩니다.

## 실행 결과(localhost:8000)

[![1571883743330](https://github.com/dwlim-nota/django-study/raw/main/day1/img/1/1571883743330.png)](https://github.com/dwlim-nota/django-study/blob/main/day1/img/1/1571883743330.png)