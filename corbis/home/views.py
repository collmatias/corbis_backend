from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q # new

from .models import Tipos_productos, Producto
from .forms import ProductoCreationForm
from .tables import ProductoTable, ProductoTableView


from django.views.generic import ListView
from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport



# Create your views here.




class ProductoListView(SingleTableView):
    model = Producto
    table_class = ProductoTable
    template_name = 'core/products.html'

class SearchResultsView(ListView):
    model = Producto
    template_name = "core/home.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")

        if not query:
            query = ''

        object_list = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(codigo__icontains=query)
        )
        return object_list

@login_required
def create_product(request):
        product_creation_form = ProductoCreationForm()

        if request.method == 'POST':
            product_creation_form = ProductoCreationForm(data=request.POST)

            if product_creation_form.is_valid():
                product_creation_form.save()
                messages.add_message(request=request, level=messages.SUCCESS, message='Producto creado correctamente')
                return redirect(reverse('home'))
            else:
                messages.add_message(request=request, level=messages.WARNING, message='Error al crear Producto')
                return redirect(reverse('home'))

        return render(request, 'core/create_product.html', {'form':product_creation_form})


@login_required
def products(request):
    prod = list(Producto.objects.values())
    return render(request, 'core/home.html', {'product_list' : prod} )
    #return render(request, 'core/products.html') """ 

@login_required
def product_details(request, buscar_producto):
    prod = get_object_or_404(Producto, nombre=buscar_producto)

    if request.method == 'GET':
        form = ProductoCreationForm(instance=prod)
        return render(request, 'core/product_detail.html', { 'producto' : prod, 'form' : form })

    else:
        form = ProductoCreationForm(request.POST, instance=prod)

        if form.is_valid():
            form.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Producto actualizado correctamente')
            return redirect(reverse('home'))
        else:
            messages.add_message(request=request, level=messages.WARNING, message='Error al editar Producto')
            return redirect(reverse('home'))


@login_required
def product_delete(request, buscar_producto):
    prod = get_object_or_404(Producto, codigo=buscar_producto)
    if request.method == 'POST':
        prod.delete()
        messages.add_message(request=request, level=messages.SUCCESS, message='Producto eliminado correctamente')
        return redirect('home')
    


def table_view(request):
    table = ProductoTableView(Producto.objects.all())

    RequestConfig(request).configure(table)

    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("table.{}".format(export_format))

    return render(request, "table.html", {
        "table": table
    })
