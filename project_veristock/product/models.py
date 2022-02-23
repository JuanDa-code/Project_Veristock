from django.db import models

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