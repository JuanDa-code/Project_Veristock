from django.db import models
from user.models import Customer, User
from .choices import estado

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    cost_sale = models.IntegerField(verbose_name='Costo Venta')
    brand = models.CharField(max_length=100, verbose_name='Marca')
    reference = models.CharField(max_length=100, verbose_name='Referencia')
    quantity = models.IntegerField(verbose_name='Cantidad', blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.brand + " " + self.reference

    class Meta:
        ordering = ['id']
        verbose_name = 'Producto'      
        
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    warranty_start = models.DateField(verbose_name='Inicio Garantia')
    warranty_end = models.DateField(verbose_name='Final Garantia')
    remarks = models.TextField(max_length=250, verbose_name='Observaciones', null=True)
    serial = models.CharField(verbose_name='Serial',max_length=30)
    state = models.CharField(verbose_name='Estado', choices=estado, max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    cost_sale = models.IntegerField(verbose_name='Costo Venta')

    def __str__(self):
        return str(self.serial)

    class Meta:
        ordering = ['serial']
        verbose_name = 'Item'

class Devolution(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name='Fecha')
    reason = models.CharField(max_length=100, verbose_name='Motivo')
    remarks = models.TextField(null=True, verbose_name='Observaciones')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, verbose_name='Item')

    def __str__(self):
        return self.reason

    class Meta:
        ordering = ['reason']
        verbose_name = 'Devolution'

class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=100, verbose_name='Descripcion')
    date = models.DateTimeField(verbose_name='Fecha')
    user = models.TextField(max_length=100, verbose_name='Usuario')

    def __str__(self):
        return self.reason

    class Meta:
        ordering = ['description']
        verbose_name = 'Logs'

class Sale(models.Model):
    invoice_number = models.AutoField(verbose_name='Numero Factura', primary_key=True)
    date = models.DateTimeField(verbose_name='Fecha')
    quantity = models.IntegerField(verbose_name='Cantidad')
    total = models.IntegerField(verbose_name='Total')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, verbose_name='Item')

    def __str__(self):
        return self.invoice_number

    class Meta:
        ordering = ['invoice_number']
        verbose_name = 'Venta'