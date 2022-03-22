from django.urls import path
from . import views

urlpatterns = [
    # Urls Position
    path('cargo/index/', views.position, name='cargo_index'),
    path('cargo/crear/', views.add_position, name='crear_cargo'),
    path('cargo/eliminar/<int:id>', views.delete_position, name='eliminar_cargo'),
    path('cargo/editar/<int:id>', views.edit_position, name='editar_cargo'),

    # Urls Type Document
    path('tipo_documento/index/', views.type_document, name='tipo_documento_index'),
    path('tipo_documento/crear/', views.add_type_document, name='crear_tipo_documento'),
    path('tipo_documento/eliminar/<int:id>', views.delete_type_document, name='eliminar_tipo_documento'),
    path('tipo_documento/editar/<int:id>', views.edit_type_document, name='editar_tipo_documento'),

    # Urls Person
    path('persona/index/', views.person, name='persona_index'),
    path('persona/crear/', views.add_person, name='crear_persona'),
    path('persona/eliminar/<int:id>', views.delete_person, name='eliminar_persona'),
    path('persona/editar/<int:id>', views.edit_person, name='editar_persona'),
]