# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abbrevation', models.CharField(max_length=2, null=True, blank=True)),
                ('name', models.CharField(max_length=250, null=True, blank=True)),
                ('capital', models.CharField(max_length=250, null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('capital_population', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
