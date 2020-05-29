from django.contrib import admin
from .models import *
from .views import *
from datetime import datetime

class DetalleCompraInline(admin.TabularInline):
	model = DetalleCompra
	extra = 1

class CompraAdmin(admin.ModelAdmin):
    actions = ['imprimir']
    inlines = [DetalleCompraInline]

    search_fields = ['proveedor']
    list_filter = ['proveedor', 'fecha']
    list_display = ['proveedor', 'fecha_de_compra', 'fecha']
    #raw_id_fields=['productos', 'proveedor']
    autocomplete_fields=['proveedor']
    readonly_fields = ['total']




class DetalleCompraAdmin(admin.ModelAdmin):
	readonly_fields = ['sub_total']
	autocomplete_fields=['productos']

admin.site.register(Compra, CompraAdmin)
#admin.site.register(DetalleCompra, DetalleCompraAdmin)
