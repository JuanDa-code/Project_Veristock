from django.db import models
from django.forms import model_to_dict
from stock.choices import estado

class Type_Document(models.Model):
    id = models.AutoField(primary_key=True)
    type_document = models.CharField(max_length=100, verbose_name='Tipo Documento')

    def __str__(self):
        return self.type_document

    class Meta:
        ordering = ['id']
        verbose_name = 'Tipo Documento'
        
class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(null=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Cargo'

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name='Primer Nombre')
    second_name = models.CharField(max_length=100, verbose_name='Segundo Nombre', null=True, blank=True)
    last_names = models.CharField(max_length=100, verbose_name='Apellidos')
    type_document = models.ForeignKey(Type_Document, on_delete=models.CASCADE, verbose_name='Tipo Documento')
    document_number = models.IntegerField(verbose_name='Número Documento')
    email_address = models.EmailField(verbose_name='Email', null=True, blank=True)
    phone = models.BigIntegerField(verbose_name='Teléfono', null=True, blank=True)
    date_birth = models.DateField(verbose_name='Fecha de Nacimiento', null=True, blank=True)
    id_position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Cargo')
    password = models.CharField(max_length=100 ,verbose_name="Contraseña")
    state = models.CharField(verbose_name='Estado', max_length=20, choices=estado)


    def __str__(self):
        return self.first_name + " " + self.last_names

    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        ordering = ['id']
        verbose_name = 'Usuario'

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name='Primer Nombre')
    second_name = models.CharField(max_length=100, verbose_name='Segundo Nombre', null=True, blank=True)
    last_names = models.CharField(max_length=100, verbose_name='Apellidos')
    type_document = models.ForeignKey(Type_Document, on_delete=models.CASCADE, verbose_name='Tipo Documento')
    document_number = models.IntegerField(verbose_name='Número Documento')
    email_address = models.EmailField(verbose_name='Email', null=True, blank=True)
    phone = models.BigIntegerField(verbose_name='Teléfono', null=True, blank=True)
    date_birth = models.DateField(verbose_name='Fecha de Nacimiento', null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_names

    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        ordering = ['id']
        verbose_name = 'Cliente'