from django import forms
from .models import Item, Product, Purchase, Sale, Provider, Devolution


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields =  '__all__'

class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields =  '__all__'
        
class DevolutionForm(forms.ModelForm):

    class Meta:
        model = Devolution
        fields =  '__all__'