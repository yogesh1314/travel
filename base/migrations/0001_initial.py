# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import base.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.ImageField(upload_to=base.models.attrphotoname)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('overview', models.CharField(max_length=1000)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('indian', models.BooleanField()),
                ('hotcount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DestinationImages',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to=base.models.destphotoname)),
                ('destination', models.ForeignKey(to='base.Destination', default=None)),
            ],
        ),
        migrations.CreateModel(
            name='HomeImages',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('destination', models.ForeignKey(to='base.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='MustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('photo', models.ImageField(upload_to=base.models.mustbuyphotoname)),
                ('destination', models.ForeignKey(to='base.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='MustEat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=1000)),
                ('price_for_two', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to=base.models.musteatphotoname)),
                ('destination', models.ForeignKey(to='base.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=5000)),
                ('creator_name', models.CharField(max_length=70)),
                ('creator_contact_no', models.IntegerField(null=True, default=91, blank=True)),
                ('creator_email', models.EmailField(max_length=254)),
                ('creator_rating', models.CharField(choices=[('5', 'Very Good'), ('4', 'Good'), ('3', 'Average'), ('2', 'Poor'), ('1', 'Very Poor')], max_length=30)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewImages',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to=base.models.reviewphotoname)),
                ('review', models.ForeignKey(to='base.Review')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.ImageField(upload_to=base.models.shoppingplacesphotoname)),
                ('destination', models.ForeignKey(to='base.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Things',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.ImageField(upload_to=base.models.things_photo_name)),
                ('destination', models.ForeignKey(to='base.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='WaysToReach',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(choices=[('AIR', 'By Air'), ('BUS', 'By Bus'), ('TRAIN', 'By Train')], max_length=10)),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.ImageField(upload_to=base.models.wtrphotoname)),
                ('destination', models.ForeignKey(to='base.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='WhenToVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('jan', models.BooleanField()),
                ('feb', models.BooleanField()),
                ('mar', models.BooleanField()),
                ('apr', models.BooleanField()),
                ('may', models.BooleanField()),
                ('jun', models.BooleanField()),
                ('jul', models.BooleanField()),
                ('aug', models.BooleanField()),
                ('sep', models.BooleanField()),
                ('oct', models.BooleanField()),
                ('nov', models.BooleanField()),
                ('dec', models.BooleanField()),
                ('destination', models.ForeignKey(to='base.Destination')),
            ],
        ),
        migrations.AddField(
            model_name='attractions',
            name='destination',
            field=models.ForeignKey(to='base.Destination'),
        ),
    ]
