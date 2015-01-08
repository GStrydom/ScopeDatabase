# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workpacks', '0003_auto_20150108_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workpack',
            name='client',
        ),
        migrations.AlterField(
            model_name='workpack',
            name='lead',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
