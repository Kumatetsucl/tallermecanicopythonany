# Generated by Django 4.1.5 on 2023-06-21 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='idUser')),
                ('rut', models.CharField(max_length=12, verbose_name='Rut')),
                ('userName', models.CharField(max_length=50, verbose_name='correo')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('contrasena', models.CharField(max_length=50, verbose_name='contrasena')),
                ('direccion', models.CharField(max_length=80, verbose_name='Direccion')),
            ],
        ),
    ]