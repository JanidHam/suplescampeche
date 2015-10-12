# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sell_date', models.DateField(auto_now_add=True)),
                ('profit', models.DecimalField(verbose_name=b'Ganancia', max_digits=5, decimal_places=2)),
                ('product', models.ForeignKey(related_name='venta_product', to='inventario.Producto')),
            ],
        ),
    ]
