# -*- encoding: utf-8 -*-
from django.db import models
from inventario.models import Producto
from clientes.models import Cliente

class Venta(models.Model):
	client    = models.ForeignKey(Cliente, related_name='venta_client')
	product   = models.ForeignKey(Producto, related_name='venta_product')
	cantidad  = models.IntegerField(verbose_name='Cantidad')
	unit_cost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Costo unitario')
	sell_date = models.DateField(verbose_name='Día de venta')
	profit    = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ganancia')

	def __unicode__(self):
		return self.product.description