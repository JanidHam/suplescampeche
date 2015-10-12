# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20150901_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='buy_date',
            field=models.DateField(verbose_name=b'D\xc3\xada de la compra'),
        ),
    ]
