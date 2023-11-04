# Generated by Django 4.1.5 on 2023-06-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mecanicosDuoc', '0002_cotizacion_alter_usuario_contrasena_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False, verbose_name='id prodcuto')),
                ('nombreProducto', models.CharField(max_length=80, verbose_name='Nombre Producto')),
                ('marcaProducto', models.CharField(max_length=80, verbose_name='Marca Producto')),
                ('Precio', models.IntegerField(verbose_name='Precio')),
                ('favorito', models.BooleanField(default=False)),
            ],
        ),
    ]