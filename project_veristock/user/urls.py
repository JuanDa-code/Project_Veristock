from django.urls import path
from . import views

urlpatterns = [
    # Urls Position
    path('cargo/index/', views.position, name='cargo_index'),
    path('cargo/crear/', views.add_position, name='crear_cargo'),
    path('cargo/eliminar/<int:id>', views.delete_position, name='eliminar_cargo'),
    path('cargo/editar/<int:id>', views.edit_position, name='editar_cargo'),
]