# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_auto_20150901_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='total_compra',
            field=models.DecimalField(verbose_name=b'Total compra', max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='partidacompra',
            name='total_partida',
            field=models.DecimalField(verbose_name=b'Total compra', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='partidacompra',
            name='unit_cost',
            field=models.DecimalField(verbose_name=b'Costo unitario', max_digits=10, decimal_places=2),
        ),
    ]
