# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20141130_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profilepic',
            field=models.CharField(default='i like eggs', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='usercode',
            field=models.CharField(default='Peaches and Cream', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
