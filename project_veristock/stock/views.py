from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from user.models import Customer
from .models import Product, Sale, Devolution, Entries
from .forms import ProductForm, SaleForm, DevolutionForm


# CRUD Product

class ProductListView(ListView):
    model = Product
    template_name = 'stock/producto/index.html'
    
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Lista de Productos'
        context['botonCrear'] = 'Crear nuevo producto'
        context['urlCrear'] = reverse_lazy('crear_producto')
        context['entries'] = Entries.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchData':
                data = []
                for i in Product.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error.'
        except Exception as e:
            data['error'] = str(e)
        
        return JsonResponse(data, safe=False)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'stock/producto/crear.html'
    success_url = reverse_lazy('producto_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Crear nuevo producto'
        context['infoH4'] = 'Información del producto'
        context['url_listar'] = reverse_lazy('producto_index')
        context['listar'] = 'Listar Productos'
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

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'stock/producto/editar.html'
    success_url = reverse_lazy('producto_index')

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Editar producto'
        context['infoH4'] = 'Información del producto'
        context['url_listar'] = reverse_lazy('producto_index')
        context['listar'] = 'Listar Productos'
        context['action'] = 'edit'
        return context

class ProductDeleteView(DeleteView):
    model = Product
    template_name = './stock/producto/eliminar.html'
    success_url = reverse_lazy('producto_index')

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
        context['titlePaginador'] = 'Eliminar un producto'
        context['infoH4'] = 'Información del producto'
        context['url_listar'] = reverse_lazy('producto_index')
        context['listar'] = 'Listar Productos'
        return context

def addStockProduct(request, id):
    product = Product.objects.get(id = id)

    if request.method == 'POST':
        stock = request.POST.get("stock")
        if int(request.POST.get("precio")) == 0:
            product.stock += int(stock)
            product.save()
            return redirect('producto_index')
        else:
            precio = request.POST.get("precio")
            product.stock += int(stock)
            product.cost_sale = int(precio)
            product.save()
            return redirect('producto_index')

    return render(request, './stock/producto/agregar_producto.html', context={'product': product})

# ciclo de la lista que tienes
# how to django save in the db a list of object<T>

# CRUD Sale

class SaleView (Sale):
    template_name = 'stock/venta/crear.html'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{'id': '', 'text': '------------'}]
                for i in Product.objects.filter(name__icontains=request.POST['term']):
                    item = i.toJson()
                    item['value'] = i.name
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

def listar_productos(request):
    busqueda = request.GET.get("buscar")
    productos = Product.objects.all()

    if busqueda:
        productos = Product.objects.filter(
            Q(name__icontains = busqueda) |
            Q(brand__icontains = busqueda) |
            Q(reference__icontains = busqueda)
        ).distinct()

    form = SaleForm(request.POST or None, request.FILES or None)

    return render(request, './stock/venta/crear.html', context = {'productos': productos, 'form': form})

def sale_register(request):
    sales = Sale.objects.all()
    customers = Customer.objects.all()
    form = SaleForm(request.POST or None, request.FILES or None)
    # if form.is_valid:
    #     form.save()
    #     return redirect('venta_index')
    return render(request, './stock/venta/index1.html', context = {'sales': sales, 'form': form, 'customers': customers})
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

class DevolutionListView(ListView):
    model = Devolution
    template_name = 'stock/devolucion/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Lista de devoluciones'
        context['botonCrear'] = 'Crear nueva devolución'
        context['urlCrear'] = reverse_lazy('crear_devolucion')
        return context
    
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Devolution.objects.get(id = request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        
        return JsonResponse(data)

class DevolutionCreateView(CreateView):
    model = Devolution
    form_class = DevolutionForm
    template_name = 'stock/devolucion/crear.html'
    success_url = reverse_lazy('devolucion_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Crear nueva devolución'
        context['infoH4'] = 'Información de la devolución'
        context['url_listar'] = reverse_lazy('devolucion_index')
        context['listar'] = 'Listar Devoluciones'
        context['action'] = 'add'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                print(form)
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

class DevolutionUpdateView(UpdateView):
    model = Devolution
    form_class = DevolutionForm
    template_name = 'stock/devolucion/editar.html'
    success_url = reverse_lazy('devolucion_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Editar devolución'
        context['infoH4'] = 'Información de la devolución'
        context['url_listar'] = reverse_lazy('devolucion_index')
        context['listar'] = 'Listar devoluciones'
        context['action'] = 'edit'
        return context

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

class DevolutionDeleteView(DeleteView):
    model = Devolution
    template_name = './stock/devolucion/eliminar.html'
    success_url = reverse_lazy('devolucion_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Eliminar una devolución'
        context['infoH4'] = 'Información de la devolución'
        context['url_listar'] = reverse_lazy('devolucion_index')
        context['listar'] = 'Listar devoluciones'
        return context