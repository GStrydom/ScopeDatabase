# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='usertype',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[((b'Lead',), b'Lead'), ((b'Admin',), b'Admin'), (b'SuperUser', b'SuperUser')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilepic',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='usercode',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
