from django.contrib import admin
from clientes.models import *

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id', 'name',  'nameP', 'phone_number')
	search_fields = ['name', 'nameP', 'phone_number']

admin.site.register(Cliente, ClienteAdmin)
