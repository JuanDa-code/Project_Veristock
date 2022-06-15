from django.urls import path
from stock.views import *
from . import views

urlpatterns = [
    # Urls Product
    path('producto/index/', ProductListView.as_view(), name='producto_index'),
    path('producto/crear/', ProductCreateView.as_view(), name='crear_producto'),
    path('producto/eliminar/<int:pk>', ProductDeleteView.as_view(), name='eliminar_producto'),
    path('producto/editar/<int:pk>', ProductUpdateView.as_view(), name='editar_producto'),

    # Urls Entries
    
    path('producto/agregar_stock/<int:id>', views.addStockProduct, name='agregar_stock'),

    # Urls Sale

    path('venta/index/', SaleListView.as_view(), name='venta_index'),
    path('venta/crear/', views.listar_productos, name='crear_venta'),
    path('venta/eliminar/<int:id>', views.delete_sale, name='eliminar_venta'),
    path('venta/editar/<int:id>', views.edit_sale, name='editar_venta'),
    
    # Urls Devolution
    path('devolucion/index/', DevolutionListView.as_view(), name='devolucion_index'),
    path('devolucion/crear/', DevolutionCreateView.as_view(), name='crear_devolucion'),
    path('devolucion/eliminar/<int:pk>', DevolutionDeleteView.as_view(), name='eliminar_devolucion'),
    path('devolucion/editar/<int:pk>', DevolutionUpdateView.as_view(), name='editar_devolucion'),
]