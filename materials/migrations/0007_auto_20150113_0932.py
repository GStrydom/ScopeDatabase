# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_lineclass11261_lineclass31011_lineclass31071_lineclass31261'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialitem',
            name='lineclass',
            field=models.ForeignKey(blank=True, to='materials.Lineclass11011', null=True),
            preserve_default=True,
        ),
    ]
