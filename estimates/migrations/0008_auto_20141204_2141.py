# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0007_auto_20141204_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimatedefaults',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 21, 41, 8, 364000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='boltupjointnormhours',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='coldcutnormhours',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='cut',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='dn',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='handlemeternormshours',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='hotcutnormhours',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='pipediameter',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='prep',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='spadejointnormhours',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='tackweldgreateighty',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pipingnorms',
            name='tackweldlesseighty',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
