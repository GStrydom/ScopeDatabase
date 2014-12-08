# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0010_auto_20141204_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberofcoldcutsbase',
            name='rigforcoldcut',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numberofhotcutsbase',
            name='rigforhotcut',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 16, 55, 46, 328000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='pipediameter',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
