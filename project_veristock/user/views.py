from django.shortcuts import redirect, render
from .models import Position, Type_Document
from .forms import PositionForm, Type_DocumentForm

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
    position = Type_Document.objects.get(id = id)
    position.delete()
    return redirect('tipo_documento_index')