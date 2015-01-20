# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0012_lineclassnames_lineclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineclassnames',
            name='lineclass',
        ),
        migrations.DeleteModel(
            name='LineclassNames',
        ),
    ]
