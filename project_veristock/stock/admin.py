from django.contrib import admin
from .models import Product, Sale, Devolution, Item


# class ProductAdmin(admin.ModelAdmin):
#     search_fields = ('name'),
#     ordering = ['name']

# class ItemAdmin(admin.ModelAdmin):
#     ordering = ['serial']
#     autocomplete_fields = ['product']

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Devolution)
admin.site.register(Item)