from django.db import models
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



class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name='Primer Nombre')
    second_name = models.CharField(max_length=100, verbose_name='Segundo Nombre')
    first_surname = models.CharField(max_length=100, verbose_name='Primer Apellido')
    second_surname = models.CharField(max_length=100, verbose_name='Segundo Apellido')
    type_document = models.ForeignKey(Type_Document, on_delete=models.CASCADE, verbose_name='Tipo Documento')
    document_number = models.CharField(max_length=100, verbose_name='Numero Documento')
    email_address = models.EmailField(verbose_name='Email')
    phone = models.BigIntegerField(verbose_name='Teléfono')
    date_birth = models.DateField(verbose_name='Fecha de Nacimiento')


    def __str__(self):
        return self.first_name

        
    class Meta:
        ordering = ['id']
        verbose_name = 'Persona'



class User(models.Model):
    id = models.AutoField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Persona')
    password = models.CharField(max_length=100 ,verbose_name="Contraseña")
    state = models.CharField(verbose_name='Estado', max_length=20, choices=estado)


    def __str__(self):
        return self.id_person.first_name + " " + self.id_person.first_surname

    class Meta:
        ordering = ['id_person']
        verbose_name = 'Usuario'


class User_Position(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Cargo')
    state = models.CharField(verbose_name='Estado', max_length=20, choices=estado)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['user']
        verbose_name = 'Cargo Usuario'



class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Persona')
    state = models.CharField(verbose_name='Estado', max_length=20, choices=estado)

    def __str__(self):
        return self.person.first_name + self.person.second_name

    class Meta:
        ordering = ['person']
        verbose_name = 'Cliente'