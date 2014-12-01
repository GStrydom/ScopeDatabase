# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
            ],
            options={
                'db_table': 'area',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
            ],
            options={
                'db_table': 'zone',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
