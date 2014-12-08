# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0011_auto_20141208_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberofjointsbase',
            name='rigforjoints',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 16, 58, 47, 110000)),
            preserve_default=True,
        ),
    ]
