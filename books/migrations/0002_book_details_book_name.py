# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-10 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_details',
            name='book_name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]