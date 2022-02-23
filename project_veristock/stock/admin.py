from curses.ascii import US
from django.contrib import admin
from .models import Person, Type_Document, User, Product, Sale, Purchase, Provider, User_Position, Position, Devolution, Customer, Item

admin.site.register(Person)
admin.site.register(Type_Document)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Purchase)
admin.site.register(Provider)
admin.site.register(User_Position)
admin.site.register(Position)
admin.site.register(Devolution)
admin.site.register(Customer)
admin.site.register(Item)