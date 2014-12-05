# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('zone_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='area',
            name='zone',
            field=models.ForeignKey(blank=True, to='areas.Zone', null=True),
            preserve_default=True,
        ),
    ]
