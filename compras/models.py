# -*- encoding: utf-8 -*-
from django.db import models
from inventario.models import Producto

PROVEEDORES_CHOICES = (
	('ND', 'NUTRITION DEPOT'),
	('SP', 'SUPLEMENT PLANET'),
)

class Compra(models.Model):
	proveedor    = models.CharField(max_length=255, verbose_name='Proveedor', choices=PROVEEDORES_CHOICES)
	total_compra = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Total compra')
	buy_date     = models.DateField(verbose_name='Día de la compra')

	def __unicode__(self):
		return str(self.id) + " - " + self.proveedor + " - " + str(self.buy_date)

class PartidaCompra(models.Model):
	compra        = models.ForeignKey(Compra, related_name='compra')
	product       = models.ForeignKey(Producto, related_name='partida_product')
	cantidad      = models.IntegerField()
	unit_cost     = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Costo unitario')
	total_partida = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total partida')