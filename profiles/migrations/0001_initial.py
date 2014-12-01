# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('userprofile_id', models.AutoField(serialize=False, primary_key=True)),
                ('profilepic', models.ImageField(upload_to='profile_images', blank=True)),
                ('usercode', models.CharField(max_length=20, blank=True)),
                ('company', models.ForeignKey(to='clients.Client')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
