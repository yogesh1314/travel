# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-12 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20160610_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='description',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='description',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='musteat',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shoppingplaces',
            name='description',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='things',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]