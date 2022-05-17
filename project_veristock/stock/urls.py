from django.urls import path
from . import views

urlpatterns = [
    # Urls Product
    path('producto/index/', views.product, name='producto_index'),
    path('producto/crear/', views.add_product, name='crear_producto'),
    path('producto/eliminar/<int:id>', views.delete_product, name='eliminar_producto'),
    path('producto/editar/<int:id>', views.edit_product, name='editar_producto'),

    # Urls Item
    path('item/index/', views.item, name='item_index'),
    path('item/crear/', views.add_item, name='crear_item'),
    path('item/eliminar/<int:id>', views.delete_item, name='eliminar_item'),
    path('item/editar/<int:id>', views.edit_item, name='edit_item'),

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