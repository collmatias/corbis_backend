import django_tables2 as tables
from .models import Producto
from django_tables2.export.views import ExportMixin

class ProductoTable(tables.Table):
    class Meta:
        model = Producto
        template_name = "django_tables2/bootstrap.html"
        fields = ("codigo", 'nombre', 'precio', 'cantidad' )

class ProductoTableView(ExportMixin, tables.SingleTableView):
    class Meta:
        model = Producto
        template_name = "django_tables2/bootstrap.html"
        fields = ("codigo", 'nombre', 'precio', 'cantidad' )