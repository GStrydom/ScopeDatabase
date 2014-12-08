# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0005_auto_20141204_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldweldsbase',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 21, 30, 2, 178000)),
            preserve_default=True,
        ),
    ]
