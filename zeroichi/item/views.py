from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Item

# Create your views here.

class ItemListView(ListView):
  model = Item
  template_name = 'item/item_list.html'

class ItemCreateView(CreateView):
  model = Item
  template_name = 'item/item_create.html'
  fields = ('title', 'address', 'size', 'purchase_price', 'estimated_profit','cost', 'project_background')
  success_url = reverse_lazy('item-list')