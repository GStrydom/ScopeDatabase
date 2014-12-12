# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workpacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Erection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('size', models.CharField(max_length=30, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('lineclass', models.ForeignKey(blank=True, to='workpacks.Lineclass', null=True)),
                ('workpack', models.ForeignKey(blank=True, to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
