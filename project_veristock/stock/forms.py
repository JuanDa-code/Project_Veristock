from django import forms
from .models import Item, Product, Sale, Devolution


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'cost_sale', 'brand', 'reference']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del producto',
        })

        self.fields['cost_sale'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el precio del producto',
        })
        
        self.fields['brand'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la Marca del Producto',
        })

        self.fields['reference'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la referencia del Producto',
        })


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['warranty_start', 'warranty_end', 'remarks', 'serial', 'state', 'product', 'cost_sale']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['warranty_start'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el inicio de la garantia',
            'type': 'date',
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
            'default': 'Seleccione una opción',
        })

        self.fields['product'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Producto',
        })

        self.fields['cost_sale'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Costo venta',
        })

class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields =  ['date', 'quantity', 'total', 'customer', 'user', 'item']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese fecha de venta',
        })

        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Cantidad',
        })

        self.fields['total'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Total',
        })

        self.fields['customer'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Ingrese el cliente',
        })

        self.fields['user'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Ingrese el usuario',
        })

        self.fields['item'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Item',
        })
        
class DevolutionForm(forms.ModelForm):

    class Meta:
        model = Devolution
        fields =  ['date', 'reason', 'remarks', 'item']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la fecha de la devolucion',
        })

        self.fields['reason'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Motivo de la devolucion',
        })

        self.fields['remarks'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Observaciones',
        })

        self.fields['item'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Item',
        })