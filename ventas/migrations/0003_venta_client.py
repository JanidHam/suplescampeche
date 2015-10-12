# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('ventas', '0002_auto_20150830_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='client',
            field=models.ForeignKey(related_name='venta_client', default=1, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]
