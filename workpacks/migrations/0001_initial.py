# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('projects', '0001_initial'),
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('lead_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('datecreated', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lineclass',
            fields=[
                ('lineclass_id', models.AutoField(serialize=False, primary_key=True)),
                ('lineclassname', models.CharField(max_length=10, blank=True)),
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
        migrations.CreateModel(
            name='Lineclasses',
            fields=[
                ('lineclasses_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workpack',
            fields=[
                ('workpack_id', models.AutoField(serialize=False, primary_key=True)),
                ('workpacknumber', models.CharField(unique=True, max_length=30, blank=True)),
                ('workpacklineclass', models.CharField(max_length=30, blank=True)),
                ('workpacklinenumber', models.CharField(max_length=30, blank=True)),
                ('datecreated', models.DateField(null=True, blank=True)),
                ('area', models.ForeignKey(blank=True, to='areas.Area', null=True)),
                ('client', models.ForeignKey(blank=True, to='clients.Client', null=True)),
                ('lead', models.ForeignKey(blank=True, to='workpacks.Lead', null=True)),
                ('project', models.ForeignKey(blank=True, to='projects.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
