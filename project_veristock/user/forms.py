from django import forms
from .models import Customer, Person, Position, Type_Document, User

class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese nombre del cargo',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Descripción del cargo',
        })

class Type_DocumentForm(forms.ModelForm):

    class Meta:
        model = Type_Document
        fields = ['type_document']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type_document'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Tipo de documento',
        })

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'second_name', 'last_names', 'type_document', 'document_number', 'email_address', 'phone', 'date_birth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields ['first_name'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Ingrese el primer nombre',
        })

        self.fields['second_name'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Ingrese el segundo nombre',
        })
        
        self.fields['last_names'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Ingrese los apellidos',
            })
        
        self.fields['type_document'].widget.attrs.update({
                'class': 'form-select',
                'placeholder': 'tipo de documento',
            })

        self.fields['document_number'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Ingrese numero de documento',
            })

        self.fields['email_address'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Ingrese el correo electronico',
            })

        self.fields['phone'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Ingrese el telefono',
            })

        self.fields['date_birth'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Ingrese fecha de nacimiento',
            })


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['id_person', 'id_position', 'password', 'state']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['id_person'].widget.attrs.update({
                'class': 'form-select',
                'placeholder':'Persona',
            })

        self.fields['id_position'].widget.attrs.update({
                'class': 'form-select',
                'placeholder':'Cargo',
            })

        self.fields['password'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Ingrese una contraseña',
            })

        self.fields['state'].widget.attrs.update({
                'class': 'form-select',
                'placeholder': 'Estado',
            })

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['person', 'state']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['person'].widget.attrs.update({
                'class': 'form-select',
                'placeholder': 'Persona',
            })

        self.fields['state'].widget.attrs.update({
                'class': 'form-select',
                'placeholder': 'Estado',
            })