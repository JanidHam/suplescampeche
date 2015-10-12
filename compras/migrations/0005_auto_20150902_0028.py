# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20150902_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partidacompra',
            name='total_partida',
            field=models.DecimalField(verbose_name=b'Total partida', max_digits=10, decimal_places=2),
        ),
    ]
