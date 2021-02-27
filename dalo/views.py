from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import StockNames

# Create your views here.
class HomePageView(ListView):
    model = StockNames
    template_name = 'home.html'
