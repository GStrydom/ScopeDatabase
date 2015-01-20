# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0009_lineclass_lineclassname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lineclass11071',
        ),
        migrations.DeleteModel(
            name='Lineclass11261',
        ),
        migrations.DeleteModel(
            name='Lineclass31011',
        ),
        migrations.DeleteModel(
            name='Lineclass31071',
        ),
        migrations.DeleteModel(
            name='Lineclass31261',
        ),
        migrations.AlterField(
            model_name='lineclass',
            name='lineclassname',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='materialitem',
            name='lineclass',
            field=smart_selects.db_fields.ChainedForeignKey(to='materials.Lineclass'),
            preserve_default=True,
        ),
    ]
