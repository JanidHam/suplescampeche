# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_producto_last_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proveedor', models.CharField(max_length=255, verbose_name=b'Proveedor', choices=[(b'ND', b'NUTRITION DEPOT'), (b'SP', b'SUPLEMENT PLANET')])),
                ('cantidad', models.IntegerField()),
                ('unit_cost', models.DecimalField(verbose_name=b'Costo unitario', max_digits=5, decimal_places=2)),
                ('total_cost', models.DecimalField(verbose_name=b'Total compra', max_digits=5, decimal_places=2)),
                ('buy_date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(related_name='compra_product', to='inventario.Producto')),
            ],
        ),
    ]
