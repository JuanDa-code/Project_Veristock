from django import forms
from .models import Product, Sale, Devolution


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'cost_sale', 'brand', 'reference', 'warranty', 'remarks', 'stock', 'state']

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

        self.fields['warranty'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Seleccione si posee garantía',
        })

        self.fields['remarks'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Observaciones del producto',
        })

        self.fields['stock'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Cantidad en Bodega',
        })

        self.fields['state'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Estado del producto',
        })

class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields =  ['date', 'totalSale', 'customer', 'user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese fecha de venta',
        })

        self.fields['totalSale'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Cantidad',
        })

        self.fields['customer'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Ingrese el cliente',
        })

        self.fields['user'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Ingrese el usuario',
        })
        
class DevolutionForm(forms.ModelForm):

    class Meta:
        model = Devolution
        fields =  ['date', 'reason', 'remarks', 'id_product']

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

        self.fields['id_product'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Observaciones',
        })