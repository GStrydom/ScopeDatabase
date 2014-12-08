# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0012_auto_20141208_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberofjointsbase',
            name='instrumentsboltup',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 17, 8, 46, 459000)),
            preserve_default=True,
        ),
    ]
