# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='type',
            field=models.CharField(max_length=255, verbose_name=b'Tipo de producto', choices=[(b'PR', b'PROTEINAS'), (b'GL', b'GLUTAMINAS'), (b'QG', b'QUEMADORES DE GRASA'), (b'MV', b'MULTI VITAMINICOS'), (b'CG', b'CUIDADO GENERAL'), (b'CR', b'CREATINAS'), (b'GP', b'GANADORES DE PESO')]),
        ),
    ]
