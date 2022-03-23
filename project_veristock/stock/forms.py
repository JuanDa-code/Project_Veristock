from dataclasses import fields
from django import forms
from .models import Product, Provider


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'