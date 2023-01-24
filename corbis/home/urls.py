"""corbis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import home, create_product, products, product_details, product_delete #, register, products
from .views import ProductoListView

urlpatterns = [
    path('', products, name='home'),
    #path('products/', products, name='products'),
    path("products/", ProductoListView.as_view(), name='products'),
    path('create_product/', create_product, name='create_product'),
    path('product_details/<str:buscar_producto>', product_details, name='product_details'),
    path('product_details/<str:buscar_producto>/delete', product_delete, name='product_delete'),
    #path('product_delete/<str:buscar_producto>', product_delete, name='product_delete'),
    #path('register/', register, name='register'),

]
