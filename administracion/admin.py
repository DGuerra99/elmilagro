from django.contrib import admin
from .models import *

class ProveedorAdmin(admin.ModelAdmin):
    
    search_fields = ['nombre']
    list_filter = ['activo']
    list_display = ['codigo','nombre', 'numero', 'direccion']

class ClienteAdmin(admin.ModelAdmin):
    
    search_fields = ['nombre']
    list_filter = ['activo', 'direccion']
    list_display = ['codigo','nombre', 'numero', 'direccion']

class ProductoAdmin(admin.ModelAdmin):
    
    search_fields = ['nombre', 'marca']
    list_filter = ['marca', 'proveedor', 'activo']
    list_display = ['codigo',  'nombre']
    #raw_id_fields=['proveedor']
    autocomplete_fields=['proveedor']

class InventarioAdmin(admin.ModelAdmin):
    
    search_fields = ['producto']
    list_display = ['producto','existencia']

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Inventario, InventarioAdmin)