from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Item
from .forms import ProductForm, ItemForm

def home(request):
    return HttpResponse("<h1>Welcome</h1>")

# CRUD Product

def product(request):
    products = Product.objects.all()
    return render(request, './stock/producto/index.html', {'products': products})

def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('producto_index')
    return render(request, './stock/producto/crear.html', {'form': form})

def edit_product(request, id):
    product = Product.objects.get(id = id)
    form = ProductForm(request.POST or None, request.FILES or None, instance = product)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('producto_index')
    return render(request, './stock/producto/editar.html', {'form': form})

def delete_product(id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('producto_index')

# CRUD Item

def item(request):
    items = Item.objects.all()
    return render(request, './stock/item/index.html', {'items': items})

def add_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('item_index')
    return render(request, './stock/item/crear.html', {'form': form})

def edit_item(request, id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, request.FILES or None, instance = item)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('item_index')
    return render(request, './stock/item/editar.html', {'form': form})

def delete_item(id):
    item = Item.objects.get(id = id)
    item.delete()
    return redirect('item_index')