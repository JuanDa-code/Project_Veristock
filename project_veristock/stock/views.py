from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Sale, Devolution, Entries
from .forms import EntriesForm, ProductForm, SaleForm, DevolutionForm


# CRUD Product

def product(request):
    products = Product.objects.all()
    return render(request, './stock/producto/index.html', context={'products': products})

def add_product(request):
    # ciclo de la lista que tienes
    # how to django save in the db a list of object<T>
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

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return redirect('producto_index')

# CRUD Entries

def entries(request):
    entries = Entries.objects.all()
    return render(request, './stock/entries/index.html', context={'entries': entries})

def add_entries(request):
    form = EntriesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # form.
        # product = Product.objects.get(id=id_product)
        form.save()
        return redirect('entradas_index')
    return render(request, './stock/entries/crear.html', {'form': form}) 

# CRUD Sale

def sale_register(request):
    sales = Sale.objects.all()
    return render(request, './stock/venta/index1.html', {'sales': sales})
    # for product in products:
    #     product.quantity = Item.objects.filter(product__id=product.id).count()
    # form = SaleForm(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('venta_index')
    

def sale(request):
    sales = Sale.objects.all()
    return render(request, './stock/venta/index.html', {'sales': sales})

def add_sale(request):
    products = Product.objects.all()
    form = SaleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('venta_index')
    return render(request, './stock/venta/crear.html', context={'form': form, 'products': products})

def delete_sale(request, id):
    sale = Sale.objects.get(id = id)
    sale.delete()
    return redirect('venta_index')

def edit_sale(request, id):
    sale = Sale.objects.get(id = id)
    form = SaleForm(request.POST or None, request.FILES or None, instance = sale)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('venta_index')
    return render(request, './stock/venta/editar.html', {'form': form})


    # CRUD Devolution

def devolution(request):
    devolutions = Devolution.objects.all()
    return render(request, './stock/devolucion/index.html', {'devolutions': devolutions})

def add_devolution(request):
    form = DevolutionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('devolucion_index')
    return render(request, './stock/devolucion/crear.html', {'form': form})

def delete_devolution(request, id):
    devolution = Devolution.objects.get(id = id)
    devolution.delete()
    return redirect('devolucion_index')

def edit_devolution(request, id):
    devolution = Devolution.objects.get(id = id)
    form = DevolutionForm(request.POST or None, request.FILES or None, instance = devolution)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('devolucion_index')
    return render(request, './stock/devolucion/editar.html', {'form': form})
