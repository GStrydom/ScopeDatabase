# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0004_auto_20141204_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldweldsbase',
            name='created',
        ),
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 21, 23, 45, 217000)),
            preserve_default=True,
        ),
    ]
