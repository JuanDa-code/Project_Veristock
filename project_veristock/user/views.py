from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Position, Type_Document, User
from .forms import UserForm, CustomerForm

def home(request):
    return render(request, './dashboard/home.html')

def landing_page(request):
    return render(request, './social/home1.html')

def base(request):
    return render(request, './dashboard/base.html')

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
    success_url = reverse_lazy('crear_usuario')

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

def edit_user(request, id):
    user = User.objects.get(id = id)
    form = UserForm(request.POST or None, request.FILES or None, instance = user)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('usuario_index')
    return render(request, './user/usuario/editar.html', {'form': form})

def delete_user(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('usuario_index')

# CRUD Customer

def customer(request):
    customers = Customer.objects.all()
    return render(request, './user/cliente/index.html', {'customers': customers})

def add_customer(request):
    form = CustomerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_index')
    return render(request, './user/cliente/crear.html', {'form': form})

def edit_customer(request, id):
    customer  = Customer.objects.get(id = id)
    form = CustomerForm(request.POST or None, request.FILES or None, instance = customer)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('cliente_index')
    return render(request, './user/cliente/editar.html', {'form': form})

def delete_customer(request, id):
    customer = Customer.objects.get(id = id)
    customer.delete()
    return redirect('cliente_index')