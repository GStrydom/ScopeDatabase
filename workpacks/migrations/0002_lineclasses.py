# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workpacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lineclasses',
            fields=[
            ],
            options={
                'db_table': 'lineclasses',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
