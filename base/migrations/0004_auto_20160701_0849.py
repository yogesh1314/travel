# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-01 08:49
from __future__ import unicode_literals

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20160701_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(default='abc.jpg', upload_to=base.models.destphotoname2),
            preserve_default=False,
        ),
    ]