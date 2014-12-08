# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0014_auto_20141208_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numberofcoldcutsbase',
            name='rigforcoldcut',
        ),
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 18, 55, 20, 72000)),
            preserve_default=True,
        ),
    ]
