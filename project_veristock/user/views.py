from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from stock.models import Entries
from .models import Customer, Position, Type_Document, User
from .forms import UserForm, CustomerForm
from django.contrib.auth.views import LoginView, LogoutView

def home(request):
    context = {
        'entries': Entries.objects.all()
    }
    return render(request, './dashboard/home.html', context)

def landing_page(request):
    return render(request, './social/home.html')

def base(request):
    context = {
        'user': request.POST['user']
    }
    return render(request, './dashboard/base.html', context)

class LoginFormView(LoginView):
    template_name = 'social/iniciar_sesion.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, './social/registrar.html', context)

# CRUD Position
    
class PositionListView(ListView):
    model = Position
    template_name = 'user/cargo/index.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Lista de Cargos'
        context['botonCrear'] = 'Crear nuevo cargo'
        context['urlCrear'] = reverse_lazy('crear_cargo')
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchData':
                data = []
                for i in Position.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error.'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

# CRUD Type Document

class Type_DocumentListView(ListView):
    model = Type_Document
    template_name = 'user/tipo_documento/index.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Tipos de documentos'
        context['urlCrear'] = reverse_lazy('crear_cargo')
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchData':
                data = []
                for i in Position.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error.'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

# CRUD User

class UserListView(ListView):
    model = User
    template_name = 'user/usuario/index.html'
    
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Lista de Usuarios'
        context['botonCrear'] = 'Crear nuevo usuario'
        context['urlCrear'] = reverse_lazy('crear_usuario')
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchData':
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error.'
        except Exception as e:
            data['error'] = str(e)
        
        return JsonResponse(data, safe=False)

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/usuario/crear.html'
    success_url = reverse_lazy('usuario_index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Crear nuevo usuario'
        context['url_listar'] = reverse_lazy('usuario_index')
        context['listar'] = 'Listar Usuarios'
        context['action'] = 'add'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
        
class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/usuario/editar.html'
    success_url = reverse_lazy('usuario_index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Editar usuario'
        context['url_listar'] = reverse_lazy('usuario_index')
        context['listar'] = 'Listar usuarios'
        context['action'] = 'edit'
        return context

class UserDeleteView(DeleteView):
    model = User
    template_name = './user/usuario/eliminar.html'
    success_url = reverse_lazy('usuario_index')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Eliminar un usuario'
        context['url_listar'] = reverse_lazy('usuario_index')
        context['listar'] = 'Listar usuarios'
        context['id'] = self.object.id
        return context

# CRUD Customer

class CustomerListView(ListView):
    model = Customer
    template_name = 'user/cliente/index.html'
    
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Lista de clientes'
        context['botonCrear'] = 'Crear nuevo cliente'
        context['urlCrear'] = reverse_lazy('crear_cliente')
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchData':
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error.'
        except Exception as e:
            data['error'] = str(e)
        
        return JsonResponse(data, safe=False)

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'user/cliente/crear.html'
    success_url = reverse_lazy('cliente_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Crear nuevo cliente'
        context['url_listar'] = reverse_lazy('cliente_index')
        context['listar'] = 'Listar clientes'
        context['action'] = 'add'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
        
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'user/cliente/editar.html'
    success_url = reverse_lazy('cliente_index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Editar cliente'
        context['url_listar'] = reverse_lazy('cliente_index')
        context['listar'] = 'Listar clientes'
        context['action'] = 'edit'
        return context

class CustomerDeleteView(DeleteView):
    model = User
    template_name = './user/cliente/eliminar.html'
    success_url = reverse_lazy('cliente_index')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Eliminar un cliente'
        context['url_listar'] = reverse_lazy('cliente_index')
        context['listar'] = 'Listar clientes'
        context['id'] = self.object.id
        return context