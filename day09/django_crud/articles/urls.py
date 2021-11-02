from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # index
    path('', views.index, name="index"),

    # # Create
    path('create/', views.create, name="create"),

    # # Read
    # path('<int:article_id>/', views.read),

    # # Update
    # path('<int:article_id>/update/', views.update),

    # # Delete
    # path('<int:article_id>/delete/', views.delete),
]