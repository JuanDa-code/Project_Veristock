from django.db import models
from user.models import Customer, User

class Devolution(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name='Fecha')
    reason = models.CharField(max_length=100, verbose_name='Motivo')
    remarks = models.TextField(null=True, verbose_name='Observaciones')

    def __str__(self):
        return self.reason

    class Meta:
        ordering = ['reason']
        verbose_name = 'Devolution'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    cost_sale = models.IntegerField(verbose_name='Costo Venta')
    brand = models.CharField(max_length=100, verbose_name='Marca')
    reference = models.CharField(max_length=100, verbose_name='Referencia')
    quantity = models.IntegerField(verbose_name='Cantidad')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Producto'


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    NIT = models.CharField(max_length=100, verbose_name='NIT')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    phone = models.BigIntegerField(verbose_name='Telefono')
    address = models.CharField(max_length=100, verbose_name='Dirección')
    email_address = models.EmailField(max_length=100, verbose_name='Email')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Proveedor'


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name='Fecha')
    quantity = models.IntegerField(verbose_name='Cantidad')
    purchase_cost = models.IntegerField(verbose_name='Costo Compra')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    invoice_number = models.IntegerField(verbose_name='Numero Factura')

    def __str__(self):
        return self.invoice_number

    class Meta:
        ordering = ['invoice_number']
        verbose_name = 'Compra'


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number = models.IntegerField(verbose_name='Numero Factura')
    date = models.DateTimeField(verbose_name='Fecha')
    quantity = models.IntegerField(verbose_name='Cantidad')
    total = models.IntegerField(verbose_name='Total')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_number

    class Meta:
        ordering = ['invoice_number']
        verbose_name = 'Venta'


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    warranty_start = models.DateField(verbose_name='Inicio Garantia')
    warranty_end = models.DateField(verbose_name='Final Garantia')
    remarks = models.TextField(max_length=250, verbose_name='Observaciones', null=True)
    serial = models.IntegerField(verbose_name='Serial')
    state = models.BinaryField(verbose_name='Estado')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    devolution = models.ForeignKey(Devolution, on_delete=models.CASCADE, null=True)
    cost_sale = models.IntegerField(verbose_name='Costo Venta')

    def __str__(self):
        return self.serial

    class Meta:
        ordering = ['serial']
        verbose_name = 'Item'