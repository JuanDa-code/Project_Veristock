from django import forms
from .models import Position, Type_Document

class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = '__all__'

class Type_DocumentForm(forms.ModelForm):

    class Meta:
        model = Type_Document
        fields = '__all__'