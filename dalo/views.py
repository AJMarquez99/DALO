from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import StockName

# Create your views here.
class HomePageView(ListView):
    model = StockName
    template_name = 'home.html'
