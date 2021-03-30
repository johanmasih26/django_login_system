from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('accounts/home',views.home,name="home_url"),
    path('',views.index,name="index"),
    path('accounts/login/',LoginView.as_view(),name="login_url"),
    path('accounts/logout/',LogoutView.as_view(next_page="home_url"),name="logout_url"),
    path('accounts/register',views.register,name="register_url")
]