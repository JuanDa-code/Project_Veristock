from django.urls import path
from stock.views import *
from . import views

urlpatterns = [
    # Urls Product
    path('producto/index/', views.product, name='producto_index'),
    path('producto/index1/', ProductListView.as_view(), name='producto_index1'),
    path('producto/crear/', views.add_product, name='crear_producto'),
    path('producto/eliminar/<int:id>', views.delete_product, name='eliminar_producto'),
    path('producto/editar/<int:id>', views.edit_product, name='editar_producto'),

    # Urls Entries
    
    path('producto/agregar_stock/<int:id>', views.addStockProduct, name='agregar_stock'),

    # Urls Sale

    path('venta/index/', views.sale, name='venta_index'),
    path('venta/index1/', views.sale_register, name='venta_index1'),
    path('venta/crear/', views.listar_productos, name='crear_venta'),
    path('venta/eliminar/<int:id>', views.delete_sale, name='eliminar_venta'),
    path('venta/editar/<int:id>', views.edit_sale, name='editar_venta'),
    
    # Urls Devolution
    path('devolucion/index/', views.devolution, name='devolucion_index'),
    path('devolucion/crear/', views.add_devolution, name='crear_devolucion'),
    path('devolucion/eliminar/<int:id>', views.delete_devolution, name='eliminar_devolucion'),
    path('devolucion/editar/<int:id>', views.edit_devolution, name='editar_devolucion'),
]