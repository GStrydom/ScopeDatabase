# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workpacks', '0001_initial'),
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('code', models.CharField(max_length=50)),
                ('lineclasses', models.ForeignKey(blank=True, to='workpacks.Lineclasses', null=True)),
                ('matlist', models.ForeignKey(to='materials.MatList')),
                ('sizelist', models.ForeignKey(to='materials.SizeList')),
                ('workpack', models.ForeignKey(blank=True, to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
