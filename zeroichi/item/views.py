from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import ItemCheckForm
from .models import Item, ItemCheck

# Create your views here.

class ItemListView(ListView):
  model = Item
  template_name = 'item/item_list.html'


class ItemCreateView(CreateView):
  form_class = ItemCheckForm
  model = Item
  template_name = 'item/item_create.html'
  fields = ('title', 'address', 'size', 'purchase_price', 'estimated_profit','cost', 'project_background')
  success_url = reverse_lazy('item-list')

class ItemCheckView(CreateView):
  model = ItemCheck
  form_class = ItemCheckForm
  template_name = 'item/itemcheck_create.html'
  success_url = reverse_lazy('item-list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['item'] = Item.objects.get(pk=self.kwargs['item_id'])
    return context

  def form_valid(self, form):
    context = self.get_context_data()
    status = form.cleaned_data['status']
    context['item'].status = int(status)
    context['item'].save()
    return super().form_valid(form)
    