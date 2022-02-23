from django.db import models
from user.models import Customer, User

class Devolution(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name='Date')
    reason = models.CharField(max_length=100, verbose_name='Reason')
    remarks = models.TextField(null=True, verbose_name='Remarks')

    def __str__(self):
        return self.reason

    class Meta:
        ordering = ['reason']
        verbose_name = 'Devolution'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    cost_sale = models.IntegerField(verbose_name='Cost Sale')
    brand = models.CharField(max_length=100, verbose_name='Brand')
    reference = models.CharField(max_length=100, verbose_name='Reference')
    quantity = models.IntegerField(verbose_name='Quantity')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    NIT = models.CharField(max_length=100, verbose_name='NIT')
    name = models.CharField(max_length=100, verbose_name='Name')
    phone = models.BigIntegerField(verbose_name='Phone')
    address = models.CharField(max_length=100, verbose_name='Address')
    email_address = models.EmailField(max_length=100, verbose_name='Email Address')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Provider'


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name='Date')
    quantity = models.IntegerField(verbose_name='Quantity')
    purchase_cost = models.IntegerField(verbose_name='Purchase Cost')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    invoice_number = models.IntegerField(verbose_name='Invoice Number')

    def __str__(self):
        return self.invoice_number

    class Meta:
        ordering = ['invoice_number']
        verbose_name = 'Purchase'


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number = models.IntegerField(verbose_name='Invoice Number')
    date = models.DateTimeField(verbose_name='Date')
    quantity = models.IntegerField(verbose_name='Quantity')
    total = models.IntegerField(verbose_name='Total')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_number

    class Meta:
        ordering = ['invoice_number']
        verbose_name = 'Sale'


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    warranty_start = models.DateField(verbose_name='Warranty Start')
    warranty_end = models.DateField(verbose_name='End Warranty')
    remarks = models.TextField(max_length=250, verbose_name='Remarks', null=True)
    serial = models.IntegerField(verbose_name='Serial')
    state = models.BinaryField(verbose_name='State')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    devolution = models.ForeignKey(Devolution, on_delete=models.CASCADE)

    def __str__(self):
        return self.serial

    class Meta:
        ordering = ['serial']
        verbose_name = 'Item'