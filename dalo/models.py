from django.db import models
from datetime import date

# Create your models here.
class StockNames(models.Model):
    symbol = models.CharField(max_length=5)
    name = models.CharField(max_length=256)
    description = models.TextField()
    keywords = models.TextField(max_length=256)
    ipo_date = models.DateField(default=date.today)
    rating = models.SmallIntegerField(null=True)


