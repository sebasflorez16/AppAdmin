
from django.urls import path
from bases.views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = "config"


urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='bases/login.html'), name='logout'),
]
