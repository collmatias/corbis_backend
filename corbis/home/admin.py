from django.contrib import admin
from .models import Tipos_productos, Producto
# Register your models here.

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('tipo_nombre', 'codigo','fecha_registro', 'fecha_update')
    search_fields = ('tipo_nombre', 'codigo','fecha_registro', 'fecha_update')
    list_filter = ('tipo_nombre', 'codigo')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'cantidad', 'fecha_registro', 'fecha_update')
    search_fields = ('nombre', 'codigo','precio', 'cantidad', 'fecha_registro', 'fecha_update')
    list_filter = ('nombre', 'codigo','precio', 'cantidad')

admin.site.register(Tipos_productos, TipoProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
