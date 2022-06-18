from django import forms
from .models import Customer, User

class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

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
                    'class': 'custom-select2 form-control',
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
            'date_birth': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione una fecha',
                    'id': 'datetimepicker',  
                }
            ),
            'id_position': forms.Select(
                attrs = {
                    'class': 'custom-select2 form-control',
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
                    'class': 'custom-select2 form-control',
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
                    'class': 'custom-select2 form-control',
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
            'date_birth': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione una fecha',
                    'id': 'datetimepicker',
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