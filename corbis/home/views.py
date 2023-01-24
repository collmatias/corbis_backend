from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .models import Tipos_productos, Producto
from .forms import ProductCreationForm
from django.views.generic import ListView

# Create your views here.

#@login_required
#def home(request):
#    return render(request,'base.html')


class ProductoListView(ListView):
    model = Producto
    template_name = 'core/products.html'

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def create_product(request):
        product_creation_form = ProductCreationForm()

        if request.method == 'POST':
            product_creation_form = ProductCreationForm(data=request.POST)

            if product_creation_form.is_valid():
                product_creation_form.save()
                return redirect(reverse('create_product')+'?ok')
            else:
                return redirect(reverse('create_product')+'?error')

        return render(request, 'core/create_product.html', {'form':product_creation_form})


@login_required
def register(request):
    data = {
        'form': ProductCreationForm()
    }

    if request.method == 'POST':
        product_creation_form = ProductCreationForm(data=request.POST)

        if product_creation_form.is_valid():
            product_creation_form.save()

            return redirect('home')

    return redirect('home')

@login_required
def products(request):
    prod = list(Producto.objects.values())
    return render(request, 'core/products.html', {'product_list':prod})
    #return render(request, 'core/products.html')
