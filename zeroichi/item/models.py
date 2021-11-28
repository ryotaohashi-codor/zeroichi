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
  STATUS_CHOICE = ((0,'申請中'),(1, '承認'),(2, '却下'))
  status = models.IntegerField(choices=STATUS_CHOICE, default=0)
  def __str__(self):
    return self.title

class ItemCheck(models.Model):
  comment = models.TextField()
  order_price = models.IntegerField()
  item = models.OneToOneField(
    Item,
    on_delete=models.CASCADE,
  )