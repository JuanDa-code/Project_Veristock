from urllib.parse import DefragResult
from django.db import models
from user.models import Customer, User 
from .choices import estado, garantia

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    cost_sale = models.IntegerField(verbose_name='Costo Venta', default=0, null=False)
    brand = models.CharField(max_length=100, verbose_name='Marca')
    reference = models.CharField(max_length=100, verbose_name='Referencia')
    warranty = models.CharField(max_length=10, choices=garantia, verbose_name='Tiempo Garantia')
    remarks = models.TextField(max_length=250, verbose_name='Observaciones', null=True)
    stock = models.IntegerField(verbose_name='Stock', default=0, null=False)
    state = models.CharField(verbose_name='Estado', choices=estado, max_length=10)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.brand, self.reference)

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

    # def save(self, *args, **kwargs):
    #     product = Product.objects.get(id=self.id_product)
    #     product.stock += self.quantity
    #     product.cost_sale += self.price
    #     product.save()
    #     return super(Entries, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = 'Entrada'

class Devolution(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name='Fecha')
    reason = models.CharField(max_length=100, verbose_name='Motivo')
    remarks = models.TextField(null=True, verbose_name='Observaciones')
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')

    def __str__(self):
        return self.reason

    class Meta:
        ordering = ['reason']
        verbose_name = 'Devolution'

class Sale(models.Model):
    invoice_number = models.AutoField(verbose_name='Numero Factura', primary_key=True)
    date = models.DateTimeField(verbose_name='Fecha')
    totalSale = models.IntegerField(verbose_name='Total Venta')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')

    def __str__(self):
        return str(self.invoice_number)

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

    class Meta:
        ordering = ['invoice_number']

class Detail_temp(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number = models.ForeignKey(Sale, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalPrice = models.IntegerField()

    def __str__(self):
        return str(self.invoice_number)

    class Meta:
        ordering = ['invoice_number']

class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=100, verbose_name='Descripcion')
    date = models.DateTimeField(verbose_name='Fecha')
    user = models.TextField(max_length=100, verbose_name='Usuario')

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['description']
        verbose_name = 'Logs'