# forms.py
from django import forms
from .models import OrderItem, LaundryItem

class OrderForm(forms.Form):
    laundry_items = forms.ModelMultipleChoiceField(queryset=LaundryItem.objects.all(), widget=forms.CheckboxSelectMultiple)
    quantity = forms.IntegerField(min_value=1)
