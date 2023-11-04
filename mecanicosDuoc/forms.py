from dataclasses import fields
from django import forms
from django.forms import ModelForm, widgets
from .models import *

# importar para poder crear el usuario en la base de datos de Django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets


class LoginForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['userName', 'contrasena']


class SigninForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo Electronico'

        }


# FORMULARIO DE COTIZACION
    # id_cotizacion = models.AutoField(primary_key=True,
    #                                  verbose_name='id Cotizacion')
    # nombre = models.charField(max_length=80,
    #                           verbose_name='Nombre Cliente')
    # telefono = models.IntegerField(max_length=9,
    #                                verbose_name='Fono Cliente')
    # mensaje = models.TextField(max_length=255,
    #                            verbose_name='Mensaje Cotizacion')
class CotizacionForm(ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre',
                  'telefono',
                  'mensaje',
                  'correo',
                  ]
        labels = {
            'nombre': 'Nombre',
            'telefono': 'Telefono',
            'correo': 'Correo Electronico',
            'mensaje': 'Mensaje'
        }


# formulario crear usuario
    # id_usuario = models.AutoField(primary_key=True,
    #                               verbose_name='idUser')
    # rut = models.CharField(max_length=12,
    #                        verbose_name='Rut')
    # userName = models.CharField(max_length=50,
    #                             verbose_name='Nombre Usuario')
    # nombre = models.CharField(max_length=50,
    #                           verbose_name='nombre')
    # contrasena = models.CharField(max_length=50,
    #                               verbose_name='Contraseña')
    # direccion = models.CharField(max_length=80,
    #                              verbose_name='Direccion')
class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  ]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreProducto', 
                  'marcaProducto', 
                  'Precio', 
                  'foto']
        
        widgets = {
            'nombreProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'marcaProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'Precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  ]
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
class SigninForm2(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
                  ]
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class CotizacionForm2(ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre',
                  'telefono',
                  'mensaje',
                  'correo',
                  'estado'
                  ]
        labels = {
            'nombre': 'Nombre',
            'telefono': 'Telefono',
            'correo': 'Correo Electronico',
            'mensaje': 'Mensaje',
            'estado':'Estado'
        }
        