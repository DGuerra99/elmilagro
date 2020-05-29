from django.contrib import admin
from .models import *

class DetalleVentaInline(admin.TabularInline):
	model = DetalleVenta
	extra = 1

class VentasAdmin(admin.ModelAdmin):
    inlines = [DetalleVentaInline]
    
    search_fields = ['cliente', 'fecha']
    list_filter = ['cliente', 'fecha']
    list_display = ['cliente', 'total','id', 'fecha']
    #raw_id_fields=['productos', 'cliente']
    autocomplete_fields=['cliente']
    readonly_fields = ['total']

admin.site.register(Venta, VentasAdmin)
