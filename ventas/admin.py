from django.contrib import admin
from ventas.models import Venta

class VentaAdmin(admin.ModelAdmin):
	list_display = ('id', 'product', 'profit', 'sell_date')
	search_fields = ['product', 'profit', 'sell_date']

admin.site.register(Venta, VentaAdmin)