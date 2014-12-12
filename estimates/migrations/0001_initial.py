# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workpacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoLengthBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineclasses', models.CharField(max_length=20)),
                ('diameter', models.CharField(max_length=20)),
                ('demolength', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldWeldsBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineclasses', models.CharField(max_length=20)),
                ('diameter', models.FloatField()),
                ('numberoffieldwelds', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('workpack', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlangePressureTestBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineclasses', models.CharField(max_length=20)),
                ('diameter', models.CharField(max_length=20)),
                ('numfpt', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('flangehndlehotcut', models.BooleanField(default=False)),
                ('alkybandc', models.BooleanField(default=False)),
                ('hacksawcutting', models.BooleanField(default=False)),
                ('fambaset', models.BooleanField(default=False)),
                ('workpack', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlangeReinstateBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineclasses', models.CharField(max_length=20)),
                ('diameter', models.CharField(max_length=20)),
                ('numfri', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('alkybandc', models.BooleanField(default=False)),
                ('fambaset', models.BooleanField(default=False)),
                ('workpack', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstallLengthBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineclasses', models.CharField(max_length=20)),
                ('diameter', models.CharField(max_length=20)),
                ('installlength', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manhoursfactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material', models.CharField(max_length=30, blank=True)),
                ('pfitter', models.FloatField(null=True, blank=True)),
                ('welder', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumberOfColdCutsBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineclasses', models.CharField(max_length=20)),
                ('diameter', models.CharField(max_length=20)),
                ('numcoldcuts', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rigforcoldcut', models.BooleanField(default=False)),
                ('workpack', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumberOfHotCutsBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineclasses', models.CharField(max_length=20)),
                ('diameter', models.CharField(max_length=20)),
                ('numhotcuts', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rigforhotcut', models.BooleanField(default=False)),
                ('workpack', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumberOfJointsBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineclasses', models.CharField(max_length=20)),
                ('diameter', models.CharField(max_length=20)),
                ('numjoints', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rigforjoints', models.BooleanField(default=False)),
                ('instrumentsboltup', models.BooleanField(default=False)),
                ('workpack', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pipingnorms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pipediameter', models.FloatField()),
                ('handlemeternormshours', models.FloatField()),
                ('hotcutnormhours', models.FloatField()),
                ('coldcutnormhours', models.FloatField()),
                ('boltupjointnormhours', models.FloatField()),
                ('spadejointnormhours', models.FloatField()),
                ('cut', models.FloatField()),
                ('prep', models.FloatField()),
                ('tackweldgreateighty', models.FloatField()),
                ('tackweldlesseighty', models.FloatField()),
                ('dn', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpadingNorms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sizes', models.FloatField(null=True, blank=True)),
                ('manhrs', models.FloatField(null=True, blank=True)),
                ('res', models.FloatField(null=True, blank=True)),
                ('durtopenclose', models.FloatField(null=True, blank=True)),
                ('cuttingfactorhw', models.FloatField(null=True, blank=True)),
                ('durationhwfactor', models.FloatField(null=True, blank=True)),
                ('alkyfactor_b_and_c_class', models.FloatField(null=True, blank=True)),
                ('duration_w_alkyfactor', models.FloatField(null=True, blank=True)),
                ('cuttingfactorhacksaw', models.FloatField(null=True, blank=True)),
                ('duration_w_hacksawfactor', models.FloatField(null=True, blank=True)),
                ('fam_bafactor', models.FloatField(null=True, blank=True)),
                ('duration_w_fam_bafactor', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
