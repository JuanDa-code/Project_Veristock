from django.urls import path
from user.views import *
from . import views
from django.contrib.auth.views import *

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('iniciar_sesion/', LoginFormView.as_view(), name='iniciar_sesion'),
    path('logout/', LogoutView.as_view(), name='cerrar_sesion'),
    path('registrar/', views.register, name='registrar'),

    # Urls User
    path('usuario/index/', UserListView.as_view(), name='usuario_index'),
    path('usuario/crear/', UserCreateView.as_view(), name='crear_usuario'),
    path('usuario/eliminar/<int:pk>', UserDeleteView.as_view(), name='eliminar_usuario'),
    path('usuario/editar/<int:pk>', UserUpdateView.as_view(), name='editar_usuario'),

    # Urls Customer
    path('cliente/index/', CustomerListView.as_view(), name='cliente_index'),
    path('cliente/crear/', CustomerCreateView.as_view(), name='crear_cliente'),
    path('cliente/eliminar/<int:pk>', CustomerDeleteView.as_view(), name='eliminar_cliente'),
    path('cliente/editar/<int:pk>', CustomerUpdateView.as_view(), name='editar_cliente'),
]