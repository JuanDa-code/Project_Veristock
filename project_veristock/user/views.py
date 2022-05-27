from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Customer, Person, Position, Type_Document, User
from .forms import PersonForm, PositionForm, Type_DocumentForm, UserForm, CustomerForm

def home(request):
    return render(request, './user/usuario/home.html')

def home1(request):
    return render(request, './social/home1.html')

def navbar(request):
    return render(request, './social/navbar.html')

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

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} ha ingresado con éxito.')
    else:
        form = UserCreationForm()

    context = { 'form': form }
    return render(request, './social/iniciar_sesion.html', context)

def login1(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} ha ingresado con éxito.')
    else:
        form = UserCreationForm()

    context = { 'form': form }
    return render(request, './social/iniciar_sesion.html', context)

# CRUD Position
    
def position(request):
    positions = Position.objects.all()
    return render(request, './user/cargo/index.html', {'positions': positions})

def add_position(request):
    form = PositionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('cargo_index')
    return render(request, './user/cargo/crear.html', {'form': form})

def edit_position(request, id):
    position = Position.objects.get(id = id)
    form = PositionForm(request.POST or None, request.FILES or None, instance = position)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('cargo_index')
    return render(request, './user/cargo/editar.html', {'form': form})

def delete_position(request, id):
    position = Position.objects.get(id = id)
    position.delete()
    return redirect('cargo_index')

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