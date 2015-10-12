# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name=b'Nombre')),
                ('nameP', models.CharField(max_length=80, verbose_name=b'Apellido Paterno')),
                ('nameM', models.CharField(max_length=80, verbose_name=b'Apellido Materno')),
                ('phone_number', models.CharField(max_length=15, verbose_name=b'Tel\xc3\xa9fono')),
                ('address', models.CharField(max_length=255, verbose_name=b'Direcci\xc3\xb3n')),
            ],
        ),
    ]
