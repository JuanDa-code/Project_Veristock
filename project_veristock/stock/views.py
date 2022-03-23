from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Provider
from .forms import ProductForm, ProviderForm

def home(request):
    return HttpResponse("<h1>Welcome</h1>")


def product(request):
    products = Product.objects.all()
    return render(request, './stock/producto/index.html', {'products': products})

def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('producto_index')
    return render(request, './stock/producto/crear.html', {'form': form})

def delete_product(id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('producto_index')

def edit_product(request, id):
    product = Product.objects.get(id = id)
    form = ProductForm(request.POST or None, request.FILES or None, instance = product)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('producto_index')
    return render(request, './stock/producto/editar.html', {'form': form})

#CRUD Provider

def provider(request):
    providers = Provider.objects.all()
    return render(request, './stock/proveedor/index.html', {'providers': providers})

def add_provider(request):
    form = ProviderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('proveedor_index')
    return render(request, './stock/proveedor/crear.html', {'form': form})

def delete_provider(id):
    provider = Provider.objects.get(id = id)
    provider.delete()
    return redirect('proveedor_index')

def edit_provider(request, id):
    provider = Provider.objects.get(id = id)
    form = ProviderForm(request.POST or None, request.FILES or None, instance = provider)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('proveedor_index')
    return render(request, './stock/proveedor/editar.html', {'form': form})
