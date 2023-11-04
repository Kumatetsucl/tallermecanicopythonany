from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cotizacion)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Detalle_compra)