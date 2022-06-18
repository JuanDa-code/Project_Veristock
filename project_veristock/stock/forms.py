from tkinter.tix import Select
from django import forms
from .models import Product, Sale, Devolution


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Product
        fields = ['name', 'cost_sale', 'brand', 'reference', 'warranty', 'time_warranty', 'stock']
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto',
                    'autofocus': True
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
                    'class': 'custom-select2 form-control',
                }
            ),
            'time_warranty': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Tiempo de garantía (Meses)',
                }
            ),
            'stock': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Cantidad en bodega',
                }
            ),
        }

    def save(self, commit = True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields =  ['date', 'totalSale', 'customer', 'user']
        widgets = {
            'date': forms.TextInput(
                attrs = {
                    'autocomplete': 'off',
                    'class': 'form-control',
                    'placeholder': 'Seleccione una fecha',
                    'id': 'datetimepicker',
                }
            ),
            'totalSale': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Valor total de la venta',
                    'readonly': True,
                }
            ),
            'customer': forms.Select(
                attrs = {
                    'class': 'custom-select2 form-control',
                }
            ),
            'user': forms.Select(
                attrs = {
                    'class': 'custom-select2 form-control'
                }
            ),
        }

class DevolutionForm(forms.ModelForm):

    class Meta:
        model = Devolution
        fields =  ['date', 'reason', 'remarks', 'id_product']
        widgets = {
            'date': forms.TextInput(
                attrs = {
                    'autocomplete': 'off',
                    'class': 'form-control',
                    'placeholder': 'Seleccione una fecha',
                    'id': 'datetimepicker',
                }
            ),
            'reason': forms.Select(
                attrs = {
                    'class': 'custom-select2 form-control',
                }
            ),
            'remarks': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Observaciones del producto'
                }
            ),
            'id_product': forms.Select(
                attrs = {
                    'class': 'custom-select2 form-control'
                }
            ),
        }

    def save(self, commit = True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data