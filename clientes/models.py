# -*- encoding: utf-8 -*-
from django.db import models

class Cliente(models.Model):
	name         = models.CharField(max_length=80, verbose_name='Nombre')
	nameP        = models.CharField(max_length=80, verbose_name='Apellido Paterno')
	nameM        = models.CharField(max_length=80, verbose_name='Apellido Materno')
	phone_number = models.CharField(max_length=15, verbose_name='Teléfono')
	address      = models.CharField(max_length=255, verbose_name='Dirección')