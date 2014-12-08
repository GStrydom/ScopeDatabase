# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0006_auto_20141204_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 21, 38, 37, 611000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='boltupjointnormhours',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='coldcutnormhours',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='cut',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='dn',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='handlemeternormshours',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='hotcutnormhours',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='pipediameter',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='prep',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='spadejointnormhours',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='tackweldgreateighty',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='tackweldlesseighty',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
