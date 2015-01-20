# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0011_auto_20150113_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineclassnames',
            name='lineclass',
            field=smart_selects.db_fields.ChainedForeignKey(to='materials.Lineclass', null=True),
            preserve_default=True,
        ),
    ]
