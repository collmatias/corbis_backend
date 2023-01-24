from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .models import Tipos_productos, Producto
from .forms import ProductoCreationForm
from .tables import ProductoTable, ProductoTableView


#from django.views.generic import ListView
from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport

# Create your views here.

#@login_required
#def home(request):
#    return render(request,'base.html')


#class ProductoListView(ListView):
class ProductoListView(SingleTableView):
    model = Producto
    table_class = ProductoTable
    template_name = 'core/products.html'

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def create_product(request):
        product_creation_form = ProductoCreationForm()

        if request.method == 'POST':
            product_creation_form = ProductoCreationForm(data=request.POST)

            if product_creation_form.is_valid():
                product_creation_form.save()
                return redirect(reverse('create_product')+'?ok')
            else:
                return redirect(reverse('create_product')+'?error')

        return render(request, 'core/create_product.html', {'form':product_creation_form})


""" @login_required
def products(request):
    prod = list(Producto.objects.values())
    return render(request, 'core/products.html', {'product_list':prod})
    #return render(request, 'core/products.html') """

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