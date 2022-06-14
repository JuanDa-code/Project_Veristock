from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Person, Position, Type_Document, User
from .forms import PersonForm, PositionForm, Type_DocumentForm, UserForm, CustomerForm

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

class PositionCreateView(CreateView):
    model = Position
    form_class = PositionForm
    template_name = 'user/cargo/crear.html'
    success_url = reverse_lazy('cargo_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Crear nuevo cargo'
        context['infoH4'] = 'Información del cargo'
        context['url_listar'] = reverse_lazy('cargo_index')
        context['listar'] = 'Listar Cargos'
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

class PositionUpdateView(UpdateView):
    model = Position
    form_class = Position
    template_name = 'user/cargo/editar.html'
    success_url = reverse_lazy('cargo_index')

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

class PositionDeleteView(DeleteView):
    model = Position
    template_name = './user/cargo/eliminar.html'
    success_url = reverse_lazy('cargo_index')

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
        context['titlePaginador'] = 'Eliminar un cargo'
        context['infoH4'] = 'Información del cargo'
        context['url_listar'] = reverse_lazy('cargo_index')
        context['listar'] = 'Listar Cargos'
        return context

# CRUD Type Document

def type_document(request):
    types_documents = Type_Document.objects.all()
    return render(request, './user/tipo_documento/index.html', {'types_documents': types_documents})

def add_type_document(request):
    form = Type_DocumentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tipo_documento_index')
    return render(request, './user/tipo_documento/crear.html', {'form': form})

def edit_type_document(request, id):
    type_document = Type_Document.objects.get(id = id)
    form = Type_DocumentForm(request.POST or None, request.FILES or None, instance = type_document)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('tipo_documento_index')
    return render(request, './user/tipo_documento/editar.html', {'form': form})

def delete_type_document(request, id):
    type_document = Type_Document.objects.get(id = id)
    type_document.delete()
    return redirect('tipo_documento_index')


# CRUD Person

def person(request):
    persons = Person.objects.all()
    return render(request, './user/persona/index.html', {'persons': persons})

def add_person(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('persona_index')
    return render(request, './user/persona/crear.html', {'form': form})

def edit_person(request, id):
    person = Person.objects.get(id = id)
    form = PersonForm(request.POST or None, request.FILES or None, instance = person)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('persona_index')
    return render(request, './user/persona/editar.html', {'form': form})

def delete_person(request, id):
    person = Person.objects.get(id = id)
    person.delete()
    return redirect('persona_index')


# CRUD User

def user(request):
    users = User.objects.all()
    return render(request, './user/usuario/index.html', {'users': users})

def add_user(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('usuario_index')
    return render(request, './user/usuario/crear.html', {'form': form})

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

# CRUD User_Position

# def user_position(request):
#     user_positions = User_Position.objects.all()
#     return render(request, './user/usuario_cargo/index.html', {'user_positions': user_positions})

# def add_user_position(request):
#     form = User_PositionForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return redirect('usuario_cargo_index')
#     return render(request, './user/usuario_cargo/crear.html', {'form': form})

# def edit_user_position(request, id):
#     user_position = User_Position.objects.get(id = id)
#     form = User_PositionForm(request.POST or None, request.FILES or None, instance = user_position)
#     if form.is_valid() and request.POST:
#         form.save()
#         return redirect('usuario_cargo_index')
#     return render(request, './user/usuario_cargo/editar.html', {'form': form})

# def delete_user_position(request, id):
#     user_position = User_Position.objects.get(id = id)
#     user_position.delete()
#     return redirect('usuario_cargo_index')