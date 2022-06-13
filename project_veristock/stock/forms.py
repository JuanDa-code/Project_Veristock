import datetime
from django import forms
from .models import Product, Sale, Devolution


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
        widgets = {
            'date': forms.DateInput(
                attrs = {
                    'autocomplete': 'off',
                    'class': 'form-control date-picker',
                    'placeholder': 'Seleccione una fecha',
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
                    'class': 'custom-select',
                }
            ),
            'user': forms.Select(
                attrs = {
                    'class': 'custom-select'
                }
            ),
        }

class DevolutionForm(forms.ModelForm):

    class Meta:
        model = Devolution
        fields =  ['date', 'reason', 'remarks', 'id_product']
        widgets = {
            'date': forms.DateTimeInput(
                attrs = {
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker',
                    'placeholder': 'Seleccione una fecha',
                }
            ),
            'reason': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Motivos de la devolución'
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
                    'class': 'custom-select'
                }
            ),
        }