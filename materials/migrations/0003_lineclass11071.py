# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_auto_20141217_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lineclass11071',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemname', models.CharField(max_length=30, blank=True)),
                ('itemid', models.CharField(max_length=10, blank=True)),
                ('material', models.CharField(max_length=20, blank=True)),
                ('dn1', models.CharField(max_length=20, blank=True)),
                ('dn2', models.CharField(max_length=20, blank=True)),
                ('code', models.CharField(max_length=30, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('unit', models.CharField(max_length=10, blank=True)),
                ('bulkquantity', models.IntegerField(null=True, blank=True)),
                ('bomunit', models.CharField(max_length=30, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
