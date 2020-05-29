from django.contrib import admin
from .models import *

class Detalle_Dev_Prov_DefInline(admin.TabularInline):
	model = Detalle_Dev_Prov_Def
	extra = 1

class DetalleDevolcionCLientesDefInline(admin.TabularInline):
	model = DetalleDevolcionCLientesDef
	extra = 1


class DetalleDevolucionesDeVentaInline(admin.TabularInline):
	model = DetalleDevolucionesDeVenta
	extra = 1
	

class DetalleDevCompraInline(admin.TabularInline):
	model = DetalleDevCompra
	extra = 1


class Inventario_DefectuososAdmin(admin.ModelAdmin):
    
    search_fields = ['producto']
    list_display = ['producto','existencia']


class Devolucion_Proveedores_DAdmin(admin.ModelAdmin):
    inlines = [Detalle_Dev_Prov_DefInline]

    search_fields = ['proveedor']
    list_filter = ['proveedor', 'fecha']
    list_display = ['proveedor', 'fecha_de_compra', 'fecha']
    #raw_id_fields=['productos', 'proveedor']
    autocomplete_fields=['proveedor']
    readonly_fields = ['total']


class Devolucion_Clienes_DefAdmin(admin.ModelAdmin):
    inlines = [DetalleDevolcionCLientesDefInline]

    search_fields = ['cliente']
    list_filter = ['cliente', 'fecha']
    list_display = ['cliente', 'fecha_de_compra', 'fecha']
    #raw_id_fields=['productos', 'proveedor']
    autocomplete_fields=['cliente']
    readonly_fields = ['total']


class DevolucionesDeVentaAdmin(admin.ModelAdmin):
	inlines = [DetalleDevolucionesDeVentaInline]
	search_fields = ['cliente']
	list_filter = ['cliente', 'fecha']
	list_display = ['cliente', 'fecha_de_compra', 'fecha']
	autocomplete_fields=['cliente']
	readonly_fields = ['total']

class DevolucionDeCompraAdmin(admin.ModelAdmin):
	inlines = [DetalleDevCompraInline]
	search_fields = ['proveedor']
	list_filter = ['proveedor', 'fecha']
	list_display = ['proveedor', 'fecha_de_compra', 'fecha']
	autocomplete_fields=['proveedor']
	readonly_fields = ['total']

admin.site.register(Devolucion_Proveedores_D, Devolucion_Proveedores_DAdmin)
admin.site.register(Devolucion_Clienes_Def, Devolucion_Clienes_DefAdmin)
admin.site.register(DevolucionesDeVenta, DevolucionesDeVentaAdmin)
admin.site.register(DevolucionDeCompra, DevolucionDeCompraAdmin)
admin.site.register(Inventario_Defectuosos, Inventario_DefectuososAdmin)
	

