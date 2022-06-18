from django.contrib import admin
from .models import Product, Sale, Devolution, Entries, Details_sale

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Devolution)
admin.site.register(Entries)
admin.site.register(Details_sale)