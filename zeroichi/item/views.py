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

class ItemCheckView(CreateView):
  model = ItemCheck
  template_name = 'item/itemcheck_create.html'
  success_url = reverse_lazy('item-list')
  fields = '__all__'

  def get_context_data(self, **kwargs):
    context = super(ItemCheckView, self).get_context_data(**kwargs)
    context['item'] = Item.objects.get(pk=self.kwargs['item_id'])
    return context

  def form_valid(self, form):
    self.object = Item.objects.get(pk=self.kwargs['item_id'])
    print(dir(form.instance.item.title))
    self.object.title = form.instance.item.title   
    self.object.save()
    return super().form_valid(form)
    