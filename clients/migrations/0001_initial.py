# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clientinformation',
            fields=[
            ],
            options={
                'db_table': 'clientinformation',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
