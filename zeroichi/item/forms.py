from django import forms

from .models import ItemCheck

class ItemCheckForm(forms.ModelForm):
  STATUS_CHOICE = ((0,'申請中'),(1, '承認'),(2, '却下'))
  status = forms.ChoiceField(choices=STATUS_CHOICE)
  
  class Meta:
    model = ItemCheck
    fields = '__all__'