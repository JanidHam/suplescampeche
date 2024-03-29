# -*- encoding: utf-8 -*-
from django.db import models

TYPE_CHOICES = (
	('PR', 'PROTEINAS'),
	('GL', 'GLUTAMINAS'),
	('QG', 'QUEMADORES DE GRASA'),
	('MV', 'MULTI VITAMINICOS'),
	('CG', 'CUIDADO GENERAL'),
	('CR', 'CREATINAS'),
	('GP', 'GANADORES DE PESO'),
)

class Producto(models.Model):
	description = models.CharField(max_length=255, verbose_name='Descripción')
	type        = models.CharField(max_length=255, verbose_name='Tipo de producto', choices=TYPE_CHOICES)
	sell_price  = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de venta')
	last_cost   = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Último costo')
	exist_stock = models.IntegerField(default=0, verbose_name='Existencia')
	create_date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.description