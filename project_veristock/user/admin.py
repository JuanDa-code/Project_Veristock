from django.contrib import admin
from .models import Person, Position, Customer, Type_Document, User, User_Position

admin.site.register(Person)
admin.site.register(Position)
admin.site.register(Customer)
admin.site.register(Type_Document)
admin.site.register(User)
admin.site.register(User_Position)