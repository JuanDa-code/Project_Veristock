from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
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

    # Urls Provider

    path('proveedor/index/', views.provider, name='proveedor_index'),
    path('proveedor/crear/', views.add_provider, name='crear_proveedor'),
    path('proveedor/eliminar/<int:id>', views.delete_provider, name='eliminar_proveedor'),
    path('proveedor/editar/<int:id>', views.edit_provider, name='editar_proveedor'),

    # Urls Purchase

    path('compra/index/', views.purchase, name='compra_index'),
    path('compra/crear/', views.add_purchase, name='crear_compra'),
    path('compra/eliminar/<int:id>', views.delete_purchase, name='eliminar_compra'),
    path('compra/editar/<int:id>', views.edit_purchase, name='editar_compra'),

    # Urls Sale

    path('venta/index/', views.sale, name='venta_index'),
    path('venta/crear/', views.add_sale, name='crear_venta'),
    path('venta/eliminar/<int:id>', views.delete_sale, name='eliminar_venta'),
    path('venta/editar/<int:id>', views.edit_sale, name='editar_venta'),
]