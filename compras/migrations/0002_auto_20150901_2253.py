# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_producto_last_cost'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartidaCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('unit_cost', models.DecimalField(verbose_name=b'Costo unitario', max_digits=5, decimal_places=2)),
                ('total_partida', models.DecimalField(verbose_name=b'Total compra', max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='total_cost',
            new_name='total_compra',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='product',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='unit_cost',
        ),
        migrations.AddField(
            model_name='partidacompra',
            name='compra',
            field=models.ForeignKey(related_name='compra', to='compras.Compra'),
        ),
        migrations.AddField(
            model_name='partidacompra',
            name='product',
            field=models.ForeignKey(related_name='partida_product', to='inventario.Producto'),
        ),
    ]
