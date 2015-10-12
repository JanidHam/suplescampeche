# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255, verbose_name=b'Descripci\xc3\xb3n')),
                ('type', models.CharField(max_length=255, verbose_name=b'Tipo de producto')),
                ('sell_price', models.DecimalField(verbose_name=b'Precio de venta', max_digits=5, decimal_places=2)),
                ('exist_stock', models.IntegerField(default=0, verbose_name=b'Existencia')),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
