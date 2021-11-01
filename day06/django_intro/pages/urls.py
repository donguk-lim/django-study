from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('page1/', views.page1),
]