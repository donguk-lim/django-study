from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # index
    path('', views.index, name="index"),

    # Create
    path('create/', views.create, name="create"),

    # Read
    path('<int:article_id>/', views.read, name="read"),

    # Update
    path('<int:article_id>/update/', views.update, name="update"),

    # Delete
    path('<int:article_id>/delete/', views.delete, name="delete"),

    # comment

    # Create
    path('<int:article_id>/comments/create/', views.comment_create, name="comment_create"),

    # Update
    path('<int:article_id>/comments/<int:comment_id>/update/', views.comment_update, name="comment_update"),

    # Delete
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comment_delete, name="comment_delete"),

]