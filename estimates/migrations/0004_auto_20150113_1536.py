# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0003_auto_20150113_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldweldsbase',
            name='numberoffieldwelds',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
