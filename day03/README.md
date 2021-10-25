# day3: get으로 요청하고 받기(query string)

## 복습([day2 링크](../day02/README.md))

- get으로 path parameter 입력 받는 방법
- emmet에 대한 간단한 예제



## 오늘 학습 내용

- get으로 요청하고 받기(query string)



## 주요 키워드

- query string
- form tag



```python
# pages/urls.py
urlpatterns = [
    path('throw/', views.throw),
    path('catch/', views.catch),
]
```



```python
# pages/views.py
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    name = request.GET.get("name") # request.GET은 dictionary로 취급하면 됨
    hobby = request.GET.get("hobby") # GET[]이 아닌 GET.get()으로 하는 이유는 키가 없는 경우에 None이 돌아오기 때문.
    context = {
        'name': name,
        'hobby': hobby,
    }
    return render(request, 'catch.html', context)
```



```html
<!-- pages/templates/pages/throw.html -->
... !+tab해서 앞 부분은 생성...
    <body>
        <form action="/catch/" method="get">
            <input type="text" name="name">
            <input type="text" name="hobby">
            <input type="submit" value="제출">
        </form>
    </body>
</html>
```

```html
<!-- pages/templates/pages/catch.html -->
... !+tab해서 앞 부분은 생성...
    <body>
      name: {{name}} <br><br>
      message1: {{hobby}}
    </body>
</html>
```



form tag에서 **method는** **http 프로토콜에서 어떤 메소드를 사용할 지**

**action은** **어떤 곳으로 요청을 보낼지** 입니다.

즉 지금의 form tag를 해석해 보면, name과 hobby(form tag는 전송할 때 name으로 구성요소들을 식별합니다.)를

`GET method를 사용해서 (현재 사용하고 있는 서버와 같은 곳의) /catch/라는 곳으로 요청을 보내라`

만약 action에 다른 주소를 넣어도 동작합니다.(예시: `http://naver.com`)



그리고 실행을 해줍니다.

```python
python manage.py runserver
```

localhost:8000/throw/

위의 주소로 접속해서 입력을 하면,

localhost:8000/catch/ 로 주소 이동을 하면서,

값이 전달된 것을 볼 수 있습니다.



### 다음 시간

- palindrome 실습(query string)
- DTL(Django Template Language)