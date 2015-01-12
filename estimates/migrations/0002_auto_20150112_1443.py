# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldweldsbase',
            name='diameter',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
