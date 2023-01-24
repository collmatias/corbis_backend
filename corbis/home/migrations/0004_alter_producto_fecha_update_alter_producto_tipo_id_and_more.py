# Generated by Django 4.1.5 on 2023-01-24 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_producto_producto_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tipos_productos', verbose_name='Tipo de producto'),
        ),
        migrations.AlterField(
            model_name='tipos_productos',
            name='fecha_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
    ]
