from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('tienda', tienda, name='tienda'),
    path('login/', login_view, name='login'),
    path('accounts/login/', login_view, name='login'),
    
    path('vistaLogeado/', vistaLogeado, name='vistaLogeado'),
    path('logout', logout, name='logout'),
    path('login/registrar', RegistroUsuario.as_view(), name='registrar'),
    # path Carrito
    path('tiendaLogeado/', tiendaLogeado, name='tiendaLogeado'),
    path("agregar/<int:producto_id>/", agregar_producto, name="Add"),
    path("eliminar/<int:producto_id>/", eliminar_producto, name="Del"),
    path("restar/<int:producto_id>/", restar_producto, name="Sub"),
    path("limpiar/", limpiar_carrito, name="Cls"),
    ##Path mantenedor Usuario
    path("vistaAdminClientes/", vistaAdminClientes, name="vistaAdminClientes"),
    path('vistaAdminClientes/agregar/', agregar_cliente_admin, name='usuario_agregar'),
    path('vistaAdminClientes/editar/<int:pk>/', editar_cliente_admin, name='usuario_modificar'),
    path('vistaAdminClientes/eliminar/<int:pk>/', eliminar_cliente_admin, name='usuario_delete'),
    
    ###MANTENEDOR Cotizaciones
    path("vistaAdminCotizacion/", vistaAdminCotizacion, name="vistaAdminCotizacion"),
    path('vistaAdminCotizacion/editar/<int:id_cotizacion>/', editar_cotizacion_admin, name='cotizacion_modificar'),
    path('vistaAdminCotizacion/eliminar/<int:id_cotizacion>/', eliminar_cotizacion_admin, name='cotizacion_delete'),
    
    ####MANTENEDOR DE PRODUCTOS
    path("vistaAdminProductos/", vistaAdminProductos, name="vistaAdminProductos"),
    path('vistaAdminProductos/agregar/', agregar_producto_admin, name='agregar_producto'),
    path('vistaAdminProductos/editar/<int:id_producto>/', editar_producto, name='editar_producto'),
    path('vistaAdminProductos/eliminar/<int:id_producto>/', eliminar_producto_admin, name='eliminar_producto'),
    
    #####prueba de compra
    path('guardarCompra/', guardar_compra, name='guardarCompra'),
    path('confirmacion/', confirmacion, name='confirmacion'),
    
    path('vistaAdminVentas/',vistaAdminVentas,name="vistaAdminVentas"),
    path('vistaAdminVentas/detalle/<int:id_compra>/', detalle_venta, name='detalle_venta'),
    path('vistaAdminVentas/eliminar/<int:id_compra>/', eliminar_venta, name='eliminar_venta'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
