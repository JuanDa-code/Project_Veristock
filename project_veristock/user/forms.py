from django import forms
from .models import Customer, User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'last_names', 'type_document', 'document_number', 'email_address', 'phone', 'date_birth', 'id_position', 'password', 'state']
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su primer nombre',
                    'autofocus': True
                }
            ),
            'second_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su segundo nombre (OPCIONAL)',
                }
            ),
            'last_names': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'type_document': forms.Select(
                attrs = {
                    'class': 'custom-select',
                }
            ),
            'document_number': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de documento',
                }
            ),
            'email_address': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                }
            ),
            'phone': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de teléfono',
                }
            ),
            'date_birth': forms.DateInput(
                attrs = {
                    'class': 'form-control date-picker',
                    'placeholder': 'Seleccione una fecha',
                }
            ),
            'id_position': forms.Select(
                attrs = {
                    'class': 'custom-select',
                }
            ),
            'password': forms.PasswordInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su contraseña',
                }
            ),
            'state': forms.Select(
                attrs = {
                    'class': 'custom-select',
                }
            ),
        }

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'second_name', 'last_names', 'type_document', 'document_number', 'email_address', 'phone', 'date_birth']
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su primer nombre',
                    'autofocus': True
                }
            ),
            'second_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su segundo nombre (OPCIONAL)',
                }
            ),
            'last_names': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'type_document': forms.Select(
                attrs = {
                    'class': 'custom-select',
                }
            ),
            'document_number': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de documento',
                }
            ),
            'email_address': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                }
            ),
            'phone': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de teléfono',
                }
            ),
            'date_birth': forms.DateInput(
                attrs = {
                    'class': 'form-control date-picker',
                    'placeholder': 'Seleccione una fecha',
                }
            ),
        }