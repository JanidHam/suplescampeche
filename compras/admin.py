from django.contrib import admin
from compras.models import *

class CompraAdmin(admin.ModelAdmin):
	list_display = ('id', 'proveedor',  'total_compra', 'buy_date')
	search_fields = ['proveedor', 'buy_date']

class PartidaCompraAdmin(admin.ModelAdmin):
	list_display = ('id', 'compra', 'product',  'cantidad', 'unit_cost', 'total_partida')
	search_fields = ['product', 'unit_cost']

admin.site.register(Compra, CompraAdmin)
admin.site.register(PartidaCompra, PartidaCompraAdmin)