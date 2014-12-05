# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('datecreated', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clientinformation',
            fields=[
                ('clientinformation_id', models.AutoField(serialize=False, primary_key=True)),
                ('contactnumber', models.IntegerField(null=True, blank=True)),
                ('email', models.CharField(max_length=50, blank=True)),
                ('address', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='client',
            name='customerinformation',
            field=models.ForeignKey(blank=True, to='clients.Clientinformation', null=True),
            preserve_default=True,
        ),
    ]
