# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_producto_last_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='last_cost',
            field=models.DecimalField(verbose_name=b'\xc3\x9altimo costo', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='producto',
            name='sell_price',
            field=models.DecimalField(verbose_name=b'Precio de venta', max_digits=10, decimal_places=2),
        ),
    ]
