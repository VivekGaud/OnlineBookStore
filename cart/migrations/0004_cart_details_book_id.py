# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-08 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20190408_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_details',
            name='book_id',
            field=models.CharField(default=0, max_length=1500),
            preserve_default=False,
        ),
    ]