# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0008_auto_20150113_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineclass',
            name='lineclassname',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
