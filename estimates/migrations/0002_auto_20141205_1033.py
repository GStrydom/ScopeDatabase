# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 10, 33, 17, 496000)),
            preserve_default=True,
        ),
    ]
