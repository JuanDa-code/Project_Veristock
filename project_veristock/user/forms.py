from django import forms
from .models import Customer, Person, Position, Type_Document, User

class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = '__all__'

class Type_DocumentForm(forms.ModelForm):

    class Meta:
        model = Type_Document
        fields = '__all__'

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'