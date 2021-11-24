from django.db import models

# Create your models here.

class Item(models.Model):
  title = models.CharField(max_length = 100)
  address = models.TextField()
  size = models.FloatField()
  purchase_price = models.IntegerField()
  estimated_profit = models.IntegerField()
  cost = models.IntegerField()
  project_background = models.TextField()
  applied_date = models.DateField(auto_now=True)