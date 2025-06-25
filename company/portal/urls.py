from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                         # Home Page (after login)
    path('signup/', views.signup, name='signup'),              # Signup Page
    path('signin/', views.signin, name='signin'),              # Signin Page
    path('logout/', views.user_logout, name='logout'),         # Logout
    path('check-username/', views.check_username, name='check_username'),  # AJAX username check
]
