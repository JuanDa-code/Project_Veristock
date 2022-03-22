from django import forms
from .models import Item, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'