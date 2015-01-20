# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0002_auto_20150112_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldweldsbase',
            name='diameter',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
