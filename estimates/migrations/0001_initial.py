# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
            ],
            options={
                'db_table': 'estimate',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manhoursfactor',
            fields=[
            ],
            options={
                'db_table': 'manhoursfactor',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pipingnorms',
            fields=[
            ],
            options={
                'db_table': 'pipingnorms',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
