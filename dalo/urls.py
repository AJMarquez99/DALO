from django.urls import path
from dalo import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('stock/<slug:symbol>=<int:pk>/', views.StockPageView.as_view(), name='stock_symbol'),
    path('get_graph', views.get_graph, name="get_graph"),
]
