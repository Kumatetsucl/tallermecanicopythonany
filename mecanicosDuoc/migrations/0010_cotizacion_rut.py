# Generated by Django 4.2.2 on 2023-07-12 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mecanicosDuoc', '0009_remove_compra_cantidad_producto_detalle_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='rut',
            field=models.CharField(default=19, max_length=12, verbose_name='Rut'),
            preserve_default=False,
        ),
    ]
