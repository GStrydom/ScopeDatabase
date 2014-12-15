# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workpacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, null=True, blank=True)),
                ('lineclass', models.CharField(blank=True, max_length=10, null=True, choices=[((11011,), 11011), ((11011,), 11071), ((11261,), 11261), ((31011,), 31011), ((31071,), 31071), (31261, 31261)])),
                ('diameter', models.CharField(max_length=5, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('code', models.CharField(max_length=20)),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('createdby', models.ForeignKey(blank=True, to='workpacks.Lead', null=True)),
                ('workpack', models.ForeignKey(blank=True, to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
