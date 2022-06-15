from django.contrib import admin
from .models import Position, Customer, Type_Document, User

admin.site.register(Position)
admin.site.register(Customer)
admin.site.register(Type_Document)
admin.site.register(User)