from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from mecanicosDuoc.Carrito import Carrito
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
# creacion de usuarios para la pagina (usuarios de django)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView


# Create your views here.

def index(request):
    if request.method == 'POST':
        formCotizacion = CotizacionForm(request.POST)
        if formCotizacion.is_valid():
            # Guardar la instancia de Cotizacion en la base de datos
            formCotizacion.save()

            # Agregar una variable al contexto para indicar que se ha guardado correctamente
            context = {'formCotizacion': formCotizacion, 'saved': True}
            return render(request, 'core/index.html', context)
    else:
        formCotizacion = CotizacionForm()

    context = {'formCotizacion': formCotizacion, 'saved': False}
    return render(request, 'core/index.html', context)



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['userName']
            password = form.cleaned_data['contrasena']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if username == 'admin':
                    login(request, user)
                    # Redirige al usuario a la página del tablero después del inicio de sesión exitoso
                    return redirect('vistaAdminClientes')
                else:
                    login(request, user)
                    # Redirige al usuario a la página del tablero después del inicio de sesión exitoso
                    return redirect('vistaLogeado')
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'loginForm': form})


def logout(request):
    auth_logout(request)  # Elimina la sesión del usuario autenticado
    return redirect('index')  # Redirecciona a la página de inicio


@login_required
def vistaLogeado(request):
    if request.method == 'POST':
        formCotizacion = CotizacionForm(request.POST)
        if formCotizacion.is_valid():
            formCotizacion.save()  # Guarda la instancia de Cotizacion en la base de datos

            # Redirige a la vista deseada después de guardar la cotización
            return redirect('index')

    else:
        formCotizacion = CotizacionForm()
    return render(request, 'core/vistaLogeado.html', {'formCotizacion': formCotizacion})


# creacion de formulario para que se cree un usuario en el admin de django
class RegistroUsuario(CreateView):
    model = User
    template_name = "core/signinUp.html"
    form_class = SigninForm2
    success_url = reverse_lazy('login')


def tienda(request):
    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }

    return render(request, 'core/tienda.html', {**datos})


@login_required
def tiendaLogeado(request):
    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }

    return render(request, 'core/tiendaLogeado.html', {**datos})


# crud productos del carrito
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.agregar(producto)
    return redirect('tiendaLogeado')


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.eliminar(producto)
    return redirect('tiendaLogeado')


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.restar(producto)
    return redirect('tiendaLogeado')


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('tiendaLogeado')


@login_required
@permission_required('auth.view_user')
def vistaAdminProductos(request):
    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }
    return render(request, 'core/vistaAdminProductos.html', {**datos})

@login_required
@permission_required('auth.view_user')
def vistaAdminCotizacion(request):
    cotizacion = Cotizacion.objects.all()

    datos = {
        'cotizacion': cotizacion
    }
    return render(request, 'core/vistaAdminCotizacion.html', {**datos})


#Vistas para administrar productos
@login_required
@permission_required('auth.view_user')
def listar_productos(request):
    # Obtiene todos los productos de la base de datos
    productos = Producto.objects.all()
    # Renderiza la plantilla 'listar_productos.html' y pasa los productos como contexto
    return render(request, 'productos/listar_productos.html', {'productos': productos})

@login_required
@permission_required('auth.view_user')
def agregar_producto_admin(request):
    if request.method == 'POST':
        # Si se recibe una solicitud POST, crea un formulario de Producto con los datos recibidos
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo producto en la base de datos
            form.save()
            # Redirecciona a la vista 'listar_productos'
            return redirect('vistaAdminProductos')
    else:
        # Si no es una solicitud POST, crea un formulario vacío de Producto
        form = ProductoForm()
    # Renderiza la plantilla 'agregar_producto.html' y pasa el formulario como contexto
    return render(request, 'core/agregar_producto.html', {'form': form})

@login_required
@permission_required('auth.view_user')
def editar_producto(request, id_producto):
    # Obtiene el producto correspondiente al id_producto proporcionado, o muestra un error 404 si no existe
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        # Si se recibe una solicitud POST, crea un formulario de Producto con los datos recibidos y la instancia del producto existente
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en el producto en la base de datos
            form.save()
            # Redirecciona a la vista 'listar_productos'
            return redirect('vistaAdminProductos')
    else:
        # Si no es una solicitud POST, crea un formulario de Producto con la instancia del producto existente
        form = ProductoForm(instance=producto)
    # Renderiza la plantilla 'editar_producto.html' y pasa el formulario y el producto como contexto
    return render(request, 'core/editar_producto.html', {'form': form, 'producto': producto})

@login_required
@permission_required('auth.view_user')
def eliminar_producto_admin(request, id_producto):
    # Obtiene el producto correspondiente al id_producto proporcionado, o muestra un error 404 si no existe
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        # Si se recibe una solicitud POST, elimina el producto de la base de datos
        producto.delete()
        # Redirecciona a la vista 'listar_productos'
        return redirect('vistaAdminProductos')
    # Renderiza la plantilla 'eliminar_producto.html' y pasa el producto como contexto
    return render(request, 'core/eliminar_producto.html', {'producto': producto})


#mantenedor clientes
@login_required
@permission_required('auth.view_user')
def vistaAdminClientes(request):
    usuarios = User.objects.all()

    datos = {
        'usuarios': usuarios
    }
    return render(request, 'core/vistaAdminClientes.html', {**datos})

@login_required
@permission_required('auth.view_user')
def eliminar_cliente_admin(request, pk):
    usuario = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('vistaAdminClientes')
    
    return render(request, 'core/usuario_delete.html', {'usuario': usuario})

@login_required
@permission_required('auth.view_user')
def editar_cliente_admin(request, pk):
    usuario = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('vistaAdminClientes')
    else:
        form = UserForm(instance=usuario)

    return render(request, 'core/usuario_modificar.html', {'form': form, 'usuario': usuario})

@login_required
@permission_required('auth.view_user')
def agregar_cliente_admin(request):
    if request.method == 'POST':
        form = SigninForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vistaAdminClientes')
    else:
        form = SigninForm2()

    return render(request, 'core/usuario_agregar.html', {'form': form})

@login_required
@permission_required('auth.view_user')
def editar_cotizacion_admin(request, id_cotizacion):
    cotizacion = get_object_or_404(Cotizacion, id_cotizacion=id_cotizacion)
    if request.method == 'POST':
        form = CotizacionForm2(request.POST, request.FILES, instance=cotizacion)
        if form.is_valid():
            form.save()
            return redirect('vistaAdminCotizacion')
    else:
        form = CotizacionForm2(instance=cotizacion)

    return render(request, 'core/cotizacion_modificar.html', {'form': form, 'cotizacion': cotizacion})

@login_required
@permission_required('auth.view_user')
def eliminar_cotizacion_admin(request, id_cotizacion):
    cotizacion = get_object_or_404(Cotizacion, id_cotizacion=id_cotizacion)
    if request.method == 'POST':
        cotizacion.delete()
        return redirect('vistaAdminCotizacion')
    
    return render(request, 'core/cotizacion_eliminar.html', {'cotizacion': cotizacion})

@login_required
def guardar_compra(request):
    if request.method == "POST":
        # Crea una instancia de Compra
        compra = Compra(Precio_total=0)
        compra.save()

        # Obtén el carrito de compras del usuario
        carrito = Carrito(request)

        # Recorre los productos en el carrito y crea instancias de Detalle_compra
        for key, values in carrito.carrito.items():
            producto_id = values["id_producto"]
            cantidad = values["Cantidad"]
            precio = values["Precio"]
            
            # Crea una instancia de Detalle_compra relacionada con la Compra y el Producto
            detalle_compra = Detalle_compra(
                producto_id=producto_id,
                compra=compra,
                cantidad_producto=cantidad,
                precio_total=precio * cantidad
            )
            detalle_compra.save()

        # Actualiza el Precio_total de la Compra
        compra.Precio_total = sum(item["Precio"] * item["Cantidad"] for item in carrito.carrito.values())
        compra.save()

        # Limpia el carrito de compras después de realizar la compra
        carrito.limpiar()

        # Redirecciona a una página de confirmación o a otra vista
        return render(request, "core/confirmacion.html")

    return render(request, "core/Venta.html")

def confirmacion(request):
    # ...
    return redirect('core/confirmacion.html')

#mantenedor Ventas
@login_required
@permission_required('auth.view_user')
def vistaAdminVentas(request):
    compra = Compra.objects.all().order_by('-id_compra')

    det_compra = Detalle_compra.objects.all()

    datos = {
        'compra': compra,
        'det_compra':det_compra
    }
    return render(request, 'core/vistaAdminVentas.html', {**datos})

@login_required
@permission_required('auth.view_user')
def detalle_venta(request, id_compra):
    compra = get_object_or_404(Compra, id_compra=id_compra)
    det_compra = Detalle_compra.objects.filter(compra=compra).order_by('-id')  # Filtra los detalles de compra relacionados con la compra
    id_compra_prueba = id_compra
    totalCompra = compra.Precio_total

    datos = {
        'compra': [compra],
        'det_compra': det_compra,
        'id_compra_prueba':id_compra_prueba,
        'totalCompra':totalCompra
    }
    return render(request, 'core/detalle_venta.html', datos)

@login_required
@permission_required('auth.view_user')
def eliminar_venta(request, id_compra):
    compra = get_object_or_404(Compra, id_compra=id_compra)
    if request.method == 'POST':
        compra.delete()
        return redirect('vistaAdminVentas')
    
    return render(request, 'core/compra_eliminar.html', {'compra': compra})