# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=b'True'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=9.99, max_digits=10, decimal_places=2),
        ),
    ]
