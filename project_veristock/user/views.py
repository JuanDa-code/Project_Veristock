from django.shortcuts import redirect, render
from .models import Person, Position, Type_Document, User, User_Position
from .forms import PersonForm, PositionForm, Type_DocumentForm, UserForm, User_PositionForm

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

def delete_position(id):
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

def delete_type_document(id):
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

def delete_person(id):
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

def delete_user(id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('usuario_index')

# CRUD User_Position

def user_position(request):
    user_positions = User_Position.objects.all()
    return render(request, './user/usuario_cargo/index.html', {'user_positions': user_positions})

def add_user_position(request):
    form = User_PositionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('usuario_cargo_index')
    return render(request, './user/usuario_cargo/crear.html', {'form': form})

def edit_user_position(request, id):
    user_position = User_Position.objects.get(id = id)
    form = User_PositionForm(request.POST or None, request.FILES or None, instance = user_position)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('usuario_cargo_index')
    return render(request, './user/usuario_cargo/editar.html', {'form': form})

def delete_user_position(id):
    user_position = User_Position.objects.get(id = id)
    user_position.delete()
    return redirect('usuario_cargo_index')