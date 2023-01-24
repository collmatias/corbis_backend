import django_tables2 as tables
from .models import Producto

class ProductoTable(tables.Table):
    class Meta:
        model = Producto
        template_name = "django_tables2/bootstrap.html"
        fields = ("codigo", 'nombre', 'precio', 'cantidad' )