# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_venta_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(verbose_name=b'Cantidad'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='sell_date',
            field=models.DateField(verbose_name=b'D\xc3\xada de venta'),
        ),
    ]
