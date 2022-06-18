from django.db import models
from django.forms import model_to_dict
from user.models import Customer, User
from .choices import estado, garantia, motivo

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    cost_sale = models.IntegerField(verbose_name='Costo Venta', default=0, null=False)
    brand = models.CharField(max_length=100, verbose_name='Marca')
    reference = models.CharField(max_length=100, verbose_name='Referencia')
    warranty = models.CharField(max_length=10, choices=garantia, verbose_name='Garantia')
    time_warranty = models.IntegerField(verbose_name='Tiempo Garantia')
    stock = models.IntegerField(verbose_name='Stock', default=0, null=False)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.brand, self.reference)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        ordering = ['id']
        verbose_name = 'Producto'
        unique_together = ('name','brand','reference')

class Entries(models.Model):
    id = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    date = models.DateField(verbose_name="Fecha de entrada de productos.")
    quantity = models.IntegerField(verbose_name="Cantidad")
    price = models.IntegerField(verbose_name="Precio")

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Entrada'

class Devolution(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='Fecha')
    reason = models.CharField(max_length=100, verbose_name='Motivo', choices=motivo)
    remarks = models.TextField(null=True, verbose_name='Observaciones')
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto en devolución')

    def __str__(self):
        return self.reason

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        ordering = ['reason']
        verbose_name = 'Devolution'

class Sale(models.Model):
    invoice_number = models.AutoField(verbose_name='Numero Factura', primary_key=True)
    date = models.DateField(verbose_name='Fecha')
    totalSale = models.IntegerField(verbose_name='Total Venta')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')

    def __str__(self):
        return str(self.invoice_number)

    def toJSON(self):
        item = model_to_dict(self)
        item['totalSale'] = int(self.totalSale)
        item['customer'] = self.customer.toJSON()
        item['user'] = self.user.toJSON()
        return item

    class Meta:
        ordering = ['invoice_number']
        verbose_name = 'Venta'

class Details_sale(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number = models.ForeignKey(Sale, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalPrice = models.IntegerField()

    def __str__(self):
        return str(self.invoice_number)

    def toJSON(self):
        item = model_to_dict(self)
        item['id_product'] = self.id_product.toJSON()
        return item

    class Meta:
        verbose_name = 'Detalle de Venta'
        ordering = ['invoice_number']