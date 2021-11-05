from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # Create
    path('signup/', views.signup, name="signup"), # GET, POST

    # Read
    path('myaccount/', views.myaccount, name="myaccount"), # GET

    # Update
    path('update_account/', views.update_account, name="update_account"), # GET, POST

    # Delete
    path('signout/', views.signout, name="signout"), # GET, POST

    # Login
    path('login/', views.user_login, name="login"), # GET, POST

    # Logout
    path('logout/', views.user_logout, name="logout"), # POST
]