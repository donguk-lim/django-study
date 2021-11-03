from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # index
    path('', views.index, name="index"),

    # # Create
    path('create/', views.create, name="create"),

    # # Read
    path('<int:article_id>/', views.read, name="read"),

    # # Update
    path('<int:article_id>/update/', views.update, name="update"),

    # # Delete
    path('<int:article_id>/delete/', views.delete, name="delete"),
]