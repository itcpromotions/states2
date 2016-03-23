# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('zip_code', models.IntegerField(null=True, blank=True)),
                ('latitude', models.FloatField(max_length=100, null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('county', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateCapital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('capital', models.CharField(max_length=100, null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('capital_population', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='state',
            old_name='abbrevation',
            new_name='abbreviation',
        ),
        migrations.RemoveField(
            model_name='state',
            name='capital',
        ),
        migrations.RemoveField(
            model_name='state',
            name='capital_population',
        ),
        migrations.RemoveField(
            model_name='state',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='state',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, to='main.State'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='main.State', null=True),
        ),
    ]
