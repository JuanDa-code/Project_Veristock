from django.shortcuts import redirect, render
from .models import Position
from .forms import PositionForm

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