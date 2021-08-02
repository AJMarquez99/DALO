from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Stock_Name, Stock_Standard_Data
from django.http import JsonResponse
from scripts import *

# Create your views here.
class HomePageView(ListView):
    model = Stock_Name
    template_name = 'home.html'

class StockPageView(DetailView):
    model = Stock_Name
    template_name = "info.html"

    def get_context_data(self, **kwargs):
        context = super(StockPageView, self).get_context_data(**kwargs)
        context['stock_data'] = Stock_Standard_Data.objects.all()
        return context
    #queryset = Individual.objects.all()

def get_graph(request):
    stock = request.GET.get( 'stock_symbol' )
    new_data = data_visualization.getGraph( stock )
    return JsonResponse( new_data, safe=False )

