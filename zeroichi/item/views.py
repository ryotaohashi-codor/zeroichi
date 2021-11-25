from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Item, ItemCheck

# Create your views here.

class ItemListView(ListView):
  model = Item
  template_name = 'item/item_list.html'

class ItemCreateView(CreateView):
  model = Item
  template_name = 'item/item_create.html'
  fields = ('title', 'address', 'size', 'purchase_price', 'estimated_profit','cost', 'project_background')
  success_url = reverse_lazy('item-list')

class ItemCheckView(UpdateView):
  model = ItemCheck
  template_name = 'item/itemcheck_update.html'
  success_url = reverse_lazy('item-list')
  fields = ('comment', 'order_price')

  def get_context_data(self, **kwargs):
    context = super(ItemCheckView, self).get_context_data(**kwargs)
    context['item'] = Item.objects.get(pk=self.kwargs['pk'])
    return context