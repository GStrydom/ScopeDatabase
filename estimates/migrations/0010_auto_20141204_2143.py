# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0009_auto_20141204_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 21, 43, 38, 31000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='pipediameter',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
    ]
