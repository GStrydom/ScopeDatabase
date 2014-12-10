# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0002_auto_20141205_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 11, 18, 4, 576000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='pipediameter',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
