from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/index/', views.product, name='producto_index'),
    path('producto/crear/', views.add_product, name='crear_producto'),
    path('producto/eliminar/<int:id>', views.delete_product, name='eliminar_producto'),
    path('producto/editar/<int:id>', views.edit_product, name='editar_producto'),


    path('proveedor/index/', views.provider, name='proveedor_index'),
    path('proveedor/crear/', views.add_provider, name='crear_proveedor'),
    path('proveedor/eliminar/<int:id>', views.delete_provider, name='eliminar_proveedor'),
    path('proveedor/editar/<int:id>', views.edit_provider, name='editar_proveedor')
]