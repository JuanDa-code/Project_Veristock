from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Product, Sale, Devolution, Entries
from .forms import ProductForm, SaleForm, DevolutionForm


# CRUD Product


# def addStockProduct(request, id):
#     product = Product.objects.get(id = id)
#     return render(request, './stock/producto/agregar_producto.html', context={'product': product})

def product(request):
    products = Product.objects.all()
    entries = Entries.objects.all()
    return render(request, './stock/producto/index.html', context={'products': products, 'entries': entries})

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

# CRUD Sale

def listar_productos(request):
    busqueda = request.GET.get("buscar")
    productos = Product.objects.all()

    if busqueda:
        productos = Product.objects.filter(
            Q(name__icontains = busqueda) |
            Q(brand__icontains = busqueda) |
            Q(reference__icontains = busqueda)
        ).distinct()

    return render(request, './stock/venta/crear.html', {'productos': productos})

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
