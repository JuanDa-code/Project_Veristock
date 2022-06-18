import datetime
import json
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.db.models import Q
from django.db import transaction
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from project_veristock.settings import STATIC_URL

from user.models import Customer, User
from .models import Product, Sale, Devolution, Entries, Details_sale
from .forms import ProductForm, SaleForm, DevolutionForm

import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa

# CRUD Product

class ProductListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = ''
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

    @method_decorator(login_required)
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

    @method_decorator(login_required)
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
        context['id'] = self.object.id
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

# CRUD Sale
class SaleListView(ListView):
    model = Sale
    template_name = 'stock/venta/index.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Lista de ventas'
        context['botonCrear'] = 'Crear nueva venta'
        context['urlCrear'] = reverse_lazy('crear_venta')
        context['urlEliminar'] = reverse_lazy('eliminar_venta')
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Sale.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                for i in Details_sale.objects.filter(invoice_number=request.POST['invoice_number']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)   

class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'stock/venta/crear.html'
    success_url = reverse_lazy('venta_index')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Product.objects.all()
        context['titlePaginador'] = 'Crear nueva venta'
        context['url_listar'] = reverse_lazy('venta_index')
        context['listar'] = 'Listar Ventas'
        context['action'] = 'add'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_productos':
                data = []
                term = request.POST['term']
                prods = Product.objects.filter(~Q(stock__exact=0), Q(name__icontains=term) | Q(brand__icontains=term) | Q(reference__icontains=term))[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name + ' ' + i.brand + ' ' + i.reference
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    sale = Sale()
                    date = datetime.datetime.strptime(vents['date'], '%d/%m/%Y')
                    sale.date = datetime.datetime.strftime(date, '%Y-%m-%d')
                    sale.user = User.objects.get(id = vents['user'])
                    sale.customer = Customer.objects.get(id = vents['customer'])
                    sale.totalSale = int(vents['totalSale'])
                    sale.save()
                    for i in vents['products']:
                        detSale = Details_sale()
                        detSale.invoice_number = Sale.objects.get(invoice_number = sale.invoice_number)
                        detSale.id_product = Product.objects.get(id = i['id'])
                        detSale.quantity = int(i['cant'])
                        product = Product.objects.get(id = detSale.id_product.id)
                        product.stock -= detSale.quantity
                        product.save()
                        detSale.totalPrice = int(i['subtotal'])
                        detSale.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class SaleDeleteView(DeleteView):
    model = Sale
    template_name = './stock/venta/eliminar.html'
    success_url = reverse_lazy('venta_index')

    @method_decorator(login_required)
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
        context['titlePaginador'] = 'Eliminar una venta'
        context['url_listar'] = reverse_lazy('venta_index')
        context['listar'] = 'Listar Ventas'
        context['id'] = self.object.invoice_number
        return context

class SaleUpdateView(UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = 'stock/venta/editar.html'
    success_url = reverse_lazy('producto_index')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Product.objects.all()
        context['titlePaginador'] = 'Edición de una venta'
        context['url_listar'] = reverse_lazy('venta_index')
        context['listar'] = 'Listar Ventas'
        context['action'] = 'edit'
        context['detProduct'] = json.dumps(self.get_details_product())
        return context

    def get_details_product(self):
        data = []
        try:
            for i in Details_sale.objects.filter(invoice_number=self.get_object().invoice_number):
                item = i.id_product.toJSON()
                item['cant'] = i.quantity
                data.append(item)
        except:
            pass
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_productos':
                data = []
                term = request.POST['term']
                prods = Product.objects.filter(~Q(stock__exact=0), Q(name__icontains=term) | Q(brand__icontains=term) | Q(reference__icontains=term))[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name + ' ' + i.brand + ' ' + i.reference
                    data.append(item)
            elif action == 'edit':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    sale = self.get_object()
                    sale.date = vents['date']
                    sale.user = User.objects.get(id = vents['user'])
                    sale.customer = Customer.objects.get(id = vents['customer'])
                    sale.totalSale = int(vents['totalSale'])
                    sale.save()
                    sale.details_sale_set.all().delete()
                    for i in vents['products']:
                        detSale = Details_sale()
                        detSale.invoice_number = Sale.objects.get(invoice_number = sale.invoice_number)
                        detSale.id_product = Product.objects.get(id = i['id'])
                        detSale.quantity = int(i['cant'])
                        product = Product.objects.get(id = detSale.id_product.id)
                        product.stock -= detSale.quantity
                        product.save()
                        detSale.totalPrice = int(i['subtotal'])
                        detSale.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Product.objects.all()
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
                reason = request.POST['reason']
                product_id = request.POST['id_product']
                product = Product.objects.get(pk = product_id)
                producto_cambio = request.POST['producto_cambio']
                if product.stock != 0:
                    if product.warranty == 'C':
                        if reason == 'I':
                            product.stock += 1
                            product.save()
                            if producto_cambio != 0:
                                product2 = Product.objects.get(pk = producto_cambio)
                                if product2.stock != 0:
                                    product2.stock -= 1
                                    product2.save()
                                    data = form.save()
                                else:
                                    data['error'] = 'El producto escogido no tiene stock.'
                        elif reason == 'F':
                            if producto_cambio != 0:
                                product2 = Product.objects.get(pk = producto_cambio)
                                if product2.stock != 0:
                                    product2.stock -= 1
                                    product2.save()
                                    data = form.save()
                                else:
                                    data['error'] = 'El producto escogido no tiene stock.'
                            data = form.save()
                        elif reason == 'S':
                            if producto_cambio != 0:
                                product2 = Product.objects.get(pk = producto_cambio)
                                if product2.stock != 0:
                                    product2.stock -= 1
                                    product2.save()
                                    data = form.save()
                                else:
                                    data['error'] = 'El producto escogido no tiene stock.'
                            data = form.save()
                    else:
                        data['error'] = 'El producto escogido no tiene garantía.'
                else:
                    data['error'] = 'El producto escogido no tiene stock.'
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Product.objects.all()
        context['titlePaginador'] = 'Editar devolución'
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
                product_id = request.POST['id_product']
                product = Product.objects.get(pk = product_id)
                if product.warranty == 'C':
                    data = form.save()
                else:
                    data['error'] = 'El producto escogido no tiene garantía.'
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

class DevolutionDeleteView(DeleteView):
    model = Devolution
    template_name = './stock/devolucion/eliminar.html'
    success_url = reverse_lazy('devolucion_index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titlePaginador'] = 'Eliminar una devolución'
        context['infoH4'] = 'Información de la devolución'
        context['url_listar'] = reverse_lazy('devolucion_index')
        context['listar'] = 'Listar devoluciones'
        context['id'] = self.object.id
        return context

class SaleInvoicePdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('stock/venta/pdf.html')
            context = {
                'sale': Sale.objects.get(pk = self.kwargs['pk']),
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('venta_index'))