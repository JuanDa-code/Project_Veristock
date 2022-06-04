from django.urls import path
from . import views

urlpatterns = [
    # Urls Product
    path('producto/index/', views.product, name='producto_index'),
    path('producto/crear/', views.add_product, name='crear_producto'),
    path('producto/eliminar/<int:id>', views.delete_product, name='eliminar_producto'),
    path('producto/editar/<int:id>', views.edit_product, name='editar_producto'),

    # Urls Entries

    path('entradas/index/', views.entries, name='entradas_index'),
    path('entradas/crear/', views.add_entries, name='crear_entradas'),

    # Urls Sale

    path('venta/index/', views.sale, name='venta_index'),
    path('venta/index1/', views.sale_register, name='venta_index1'),
    path('venta/crear/', views.add_sale, name='crear_venta'),
    path('venta/eliminar/<int:id>', views.delete_sale, name='eliminar_venta'),
    path('venta/editar/<int:id>', views.edit_sale, name='editar_venta'),
    
    # Urls Devolution
    path('devolucion/index/', views.devolution, name='devolucion_index'),
    path('devolucion/crear/', views.add_devolution, name='crear_devolucion'),
    path('devolucion/eliminar/<int:id>', views.delete_devolution, name='eliminar_devolucion'),
    path('devolucion/editar/<int:id>', views.edit_devolution, name='editar_devolucion'),
]