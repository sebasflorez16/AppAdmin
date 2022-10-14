from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import *


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'bases/home.html'
    login_url = 'config:login'