# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20150830_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='last_cost',
            field=models.DecimalField(default=1, verbose_name=b'\xc3\x9altimo costo', max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
