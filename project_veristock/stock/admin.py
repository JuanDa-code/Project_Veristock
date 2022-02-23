from curses.ascii import US
from django.contrib import admin
from .models import Product, Sale, Purchase, Provider, Devolution, Item


admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Purchase)
admin.site.register(Provider)
admin.site.register(Devolution)
admin.site.register(Item)