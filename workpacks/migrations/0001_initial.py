# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
            ],
            options={
                'db_table': 'lead',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lineclass',
            fields=[
            ],
            options={
                'db_table': 'lineclass',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workpack',
            fields=[
            ],
            options={
                'db_table': 'workpack',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
