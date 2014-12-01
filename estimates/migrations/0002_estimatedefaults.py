# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstimateDefaults',
            fields=[
            ],
            options={
                'db_table': 'estimatedefaults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
