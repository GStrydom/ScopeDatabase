# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0013_auto_20141208_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpadingNorms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sizes', models.FloatField(null=True, blank=True)),
                ('manhrs', models.FloatField(null=True, blank=True)),
                ('res', models.FloatField(null=True, blank=True)),
                ('durtopenclose', models.FloatField(null=True, blank=True)),
                ('cuttingfactorhw', models.FloatField(null=True, blank=True)),
                ('durationhwfactor', models.FloatField(null=True, blank=True)),
                ('alkyfactor_b_and_c_class', models.FloatField(null=True, blank=True)),
                ('duration_w_alkyfactor', models.FloatField(null=True, blank=True)),
                ('cuttingfactorhacksaw', models.FloatField(null=True, blank=True)),
                ('duration_w_hacksawfactor', models.FloatField(null=True, blank=True)),
                ('fam_bafactor', models.FloatField(null=True, blank=True)),
                ('duration_w_fam_bafactor', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 18, 9, 45, 541000)),
            preserve_default=True,
        ),
    ]
