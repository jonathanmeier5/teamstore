# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-22 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamstore', '0002_auto_20170622_1139'),
        ('product', '0034_auto_20170622_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclass',
            name='team',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='teamstore.TeamStore'),
        ),
        migrations.AlterField(
            model_name='category',
            name='team',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='teamstore.TeamStore'),
        ),
        migrations.AlterField(
            model_name='product',
            name='team',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='teamstore.TeamStore'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='team',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='product_variants', to='teamstore.TeamStore'),
        ),
    ]