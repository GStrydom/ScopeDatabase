# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0013_auto_20150113_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialitem',
            name='createdby',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
