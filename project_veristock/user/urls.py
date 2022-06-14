from django.urls import path
from user.views import *
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.landing_page, name='home1'),
    path('home', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('iniciar_sesion/', LoginView.as_view(template_name='social/iniciar_sesion.html'), name='iniciar_sesion'),
    path('registrar/', views.register, name='registrar'),

    # Urls Position
    path('cargo/index/', PositionListView.as_view(), name='cargo_index'),
    path('cargo/crear/', PositionCreateView.as_view(), name='crear_cargo'),
    path('cargo/eliminar/<int:pk>', PositionDeleteView.as_view(), name='eliminar_cargo'),
    path('cargo/editar/<int:pk>', PositionUpdateView.as_view(), name='editar_cargo'),

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

    # Urls User
    path('usuario/index/', views.user, name='usuario_index'),
    path('usuario/crear/', views.add_user, name='crear_usuario'),
    path('usuario/eliminar/<int:id>', views.delete_user, name='eliminar_usuario'),
    path('usuario/editar/<int:id>', views.edit_user, name='editar_usuario'),

    # Urls Customer
    path('cliente/index/', views.customer, name='cliente_index'),
    path('cliente/crear/', views.add_customer, name='crear_cliente'),
    path('cliente/eliminar/<int:id>', views.delete_customer, name='eliminar_cliente'),
    path('cliente/editar/<int:id>', views.edit_customer, name='editar_cliente'),

    # Urls User Position
    # path('usuario_cargo/index/', views.user_position, name='usuario_cargo_index'),
    # path('usuario_cargo/crear/', views.add_user_position, name='crear_usuario_cargo'),
    # path('usuario_cargo/eliminar/<int:id>', views.delete_user_position, name='eliminar_usuario_cargo'),
    # path('usuario_cargo/editar/<int:id>', views.edit_user_position, name='editar_usuario_cargo'),
]