# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('userprofile_id', models.AutoField(serialize=False, primary_key=True)),
                ('profilepic', models.CharField(default='i like eggs', max_length=255, blank=True)),
                ('usercode', models.CharField(default='Peaches and Cream', max_length=20, blank=True)),
                ('company', models.ForeignKey(to='clients.Client')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
