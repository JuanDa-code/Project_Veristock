from django.db import models


class Type_Document(models.Model):
    id = models.AutoField(primary_key=True)
    type_document = models.CharField(max_length=100, verbose_name='Type Document')

    def __str__(self):
        return self.type_document

    class Meta:
        ordering = ['type_document']
        verbose_name = 'Type Document'



class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(null=True, verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Position'



class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    second_name = models.CharField(max_length=100, verbose_name='Second Name')
    first_surname = models.CharField(max_length=100, verbose_name='First Surname')
    second_surname = models.CharField(max_length=100, verbose_name='Second Surname')
    type_document = models.ForeignKey(Type_Document, on_delete=models.CASCADE)
    document_number = models.CharField(max_length=100, verbose_name='Document Number')
    email_address = models.EmailField(verbose_name='Email Address')
    phone = models.BigIntegerField(verbose_name='Phone')
    date_birth = models.DateField(verbose_name='Date of Birth')


    def __str__(self):
        return self.first_name

        
    class Meta:
        ordering = ['document_number']
        verbose_name = 'Person'



class User(models.Model):
    id = models.AutoField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_person

    class Meta:
        ordering = ['id_person']
        verbose_name = 'User'


class User_Position(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    state = models.BinaryField(verbose_name='State')

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['user']
        verbose_name = 'User Position'



class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person

    class Meta:
        ordering = ['person']
        verbose_name = 'Customer'



