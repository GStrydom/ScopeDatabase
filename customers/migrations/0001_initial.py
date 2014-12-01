# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customerinformation',
            fields=[
            ],
            options={
                'db_table': 'customerinformation',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
