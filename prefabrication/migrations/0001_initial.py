# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workpacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefabrication',
            fields=[
                ('prefabrication_id', models.AutoField(serialize=False, primary_key=True)),
                ('matlist', models.CharField(max_length=50, blank=True)),
                ('sizelist', models.CharField(max_length=50, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('code', models.CharField(max_length=50)),
                ('lineclasses', models.ForeignKey(to='workpacks.Lineclasses')),
                ('workpack', models.ForeignKey(blank=True, to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
