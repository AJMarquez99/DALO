from django.db import models
from datetime import date

# Create your models here.
class Stock_Name(models.Model):
    symbol = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    keywords = models.TextField(max_length=256, blank=True)
    ipo_date = models.DateField(default=date.today)
    rating = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.symbol

class Stock_Standard_Data(models.Model):
    stock = models.ForeignKey(Stock_Name, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    open = models.DecimalField(max_digits=14, decimal_places=7)
    high = models.DecimalField(max_digits=14, decimal_places=7)
    low = models.DecimalField(max_digits=14, decimal_places=7)
    close = models.DecimalField(max_digits=14, decimal_places=7)
    adjust_close = models.DecimalField(max_digits=14, decimal_places=7)
    volume = models.PositiveIntegerField()

    def __str__(self):
        return self.stock_id + " " + self.date

    # Date,Open,High,Low,Close,Adj Close,Volume


