from tkinter.tix import Select
from unicodedata import name
from xml.dom import ValidationErr
from django import forms
from .models import Entries, Product, Sale, Devolution


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto',
                }
            ),
            'cost_sale': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Precio del producto',
                }
            ),
            'brand': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Marca del producto',
                }
            ),
            'reference': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Referencia del producto',
                }
            ),
            'warranty': forms.Select(
                attrs = {
                    'class': 'custom-select',
                }
            ),
            'remarks': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Observaciones del producto',
                }
            ),
            'stock': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Cantidad en bodega',
                }
            ),
            'state': forms.Select(
                attrs = {
                    'class': 'custom-select',
                }
            ),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        if Product.objects.filter(name=cleaned_data['name'], brand=cleaned_data['brand'], reference=cleaned_data['reference']):
            raise forms.ValidationError('El producto ya existe')

        return cleaned_data

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

class EntriesForm(forms.ModelForm):

    class Meta:
        model = Entries
        fields =  ['id_product', 'date', 'quantity', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_product'].widget.attrs.update({
            'class': 'custom-select',
        })

        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Seleccione la fecha',
        })

        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Cantidad',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Precio',
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