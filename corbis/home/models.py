from django.db import models
import datetime

# Create your models here.
class Tipos_productos(models.Model):
    tipo_id = models.AutoField (primary_key=True,auto_created=True, verbose_name='Id del tipo de producto')
    codigo = models.CharField(max_length=50, unique=True, verbose_name='Codigo del tipo de producto')
    tipo_nombre = models.CharField(max_length=100, verbose_name='Tipo de producto')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de carga del registro')
    fecha_update = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualizacion')

    def __str__(self):
        return self.tipo_nombre

class Producto(models.Model):
    producto_id = models.AutoField (primary_key=True, auto_created=True, verbose_name='Id del producto')
    codigo = models.CharField(max_length=50, unique=True, verbose_name='Codigo de producto')
    nombre = models.CharField(max_length=100, verbose_name='Nombre del producto')
    tipo_id = models.ForeignKey(Tipos_productos, on_delete=models.CASCADE, verbose_name='Tipo de producto')
    precio = models.FloatField(default=0, verbose_name='Precio del producto')
    cantidad = models.IntegerField(default=0, verbose_name='Cantidad en Stock')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de carga del registro')
    fecha_update = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualizacion')

    def __str__(self):
        return self.nombre

    """     def get_string_fields(self):
        # list of some excluded fields
        excluded_fields = ['producto_id', 'id']

        # getting all fields that available in `Client` model,
        # but not in `excluded_fields`
        field_names = [field.name for field in Producto._meta.get_fields() 
                       if field.name not in excluded_fields]
        values = []
        for field_name in field_names:
            # get specific value from instanced object.
            # and outputing as `string` value.
            values.append('%s' % getattr(self, field_name))

        # joining all string values.
        return ' | '.join(values) """