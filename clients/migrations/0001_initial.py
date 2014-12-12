# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_name', models.CharField(max_length=50, null=True, blank=True)),
                ('client_contactnumber', models.IntegerField(null=True, blank=True)),
                ('client_email', models.CharField(max_length=50, null=True, blank=True)),
                ('client_address', models.CharField(max_length=255, null=True, blank=True)),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('client_project', models.ForeignKey(to='projects.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
