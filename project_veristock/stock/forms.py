from django import forms
from .models import Item, Product, Purchase, Sale, Provider, Devolution


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['warranty_start', 'warranty_end', 'remarks', 'serial', 'state', 'product', 'purchase', 'cost_sale']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['warranty_start'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el inicio de la garantia',
        })

        self.fields['warranty_end'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el final de la garantia',
        })

        self.fields['remarks'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Observaciones',
        })

        self.fields['serial'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Serial',
        })

        self.fields['state'].widget.attrs.update({
            'class': 'form-select',
            'selected': 'Selecione el estado',
        })

        self.fields['product'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Producto',
        })

        self.fields['purchase'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Compra',
        })

        self.fields['cost_sale'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Costo venta',
        })
        
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