# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('workpacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoLengthBase',
            fields=[
                ('demolengthbase_id', models.AutoField(serialize=False, primary_key=True)),
                ('lineclasses_id', models.CharField(max_length=20)),
                ('diameter_id', models.CharField(max_length=20)),
                ('demolength', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack_id', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DemoLengthHours',
            fields=[
                ('demolengthhours_id', models.AutoField(serialize=False, primary_key=True)),
                ('resources', models.SmallIntegerField(blank=True)),
                ('manhours', models.FloatField(blank=True)),
                ('duration', models.FloatField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack_id', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('estimate_id', models.AutoField(serialize=False, primary_key=True)),
                ('manhours', models.IntegerField(null=True, blank=True)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('resources', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(unique=True, max_length=255, blank=True)),
                ('workpack', models.ForeignKey(blank=True, to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstimateDefaults',
            fields=[
                ('estimatedefaults_id', models.AutoField(serialize=False, primary_key=True)),
                ('diameter', models.IntegerField()),
                ('schedule', models.CharField(max_length=10, blank=True)),
                ('material', models.CharField(max_length=10, blank=True)),
                ('fieldwelds', models.SmallIntegerField(blank=True)),
                ('demolength', models.SmallIntegerField(blank=True)),
                ('installlength', models.SmallIntegerField(blank=True)),
                ('flangesforisolation', models.SmallIntegerField(blank=True)),
                ('flangesforreinstate', models.SmallIntegerField(blank=True)),
                ('flangehandlinghotcuts', models.BooleanField(default=False)),
                ('flangehandlingalky', models.BooleanField(default=False)),
                ('flangehandlinghacksaw', models.BooleanField(default=False)),
                ('flangehandlingbaset', models.BooleanField(default=False)),
                ('numberofjoints', models.SmallIntegerField(blank=True)),
                ('instrumentsforboltup', models.BooleanField(default=False)),
                ('riggersforboltup', models.BooleanField(default=False)),
                ('numberofcoldcuts', models.SmallIntegerField(blank=True)),
                ('numberofhotcuts', models.SmallIntegerField(blank=True)),
                ('datecreated', models.DateTimeField(default=datetime.datetime(2014, 12, 4, 20, 53, 52, 229000))),
                ('lineclasses', models.ForeignKey(to='workpacks.Lineclasses')),
                ('workpack', models.ForeignKey(to='workpacks.Workpack')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldWeldsBase',
            fields=[
                ('fieldweld_id', models.AutoField(serialize=False, primary_key=True)),
                ('lineclasses_id', models.CharField(max_length=20)),
                ('diameter_id', models.FloatField()),
                ('numberoffieldwelds', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack_id', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldWeldsHours',
            fields=[
                ('fieldweldshours_id', models.AutoField(serialize=False, primary_key=True)),
                ('resources', models.SmallIntegerField(blank=True)),
                ('manhours', models.FloatField(blank=True)),
                ('duration', models.FloatField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fieldweldbase', models.ForeignKey(blank=True, to='estimates.FieldWeldsBase', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlangePressureTestBase',
            fields=[
                ('fptbase_id', models.AutoField(serialize=False, primary_key=True)),
                ('lineclasses_id', models.CharField(max_length=20)),
                ('diameter_id', models.CharField(max_length=20)),
                ('numfpt', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack_id', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlangeReinstateBase',
            fields=[
                ('fribase_id', models.AutoField(serialize=False, primary_key=True)),
                ('lineclasses_id', models.CharField(max_length=20)),
                ('diameter_id', models.CharField(max_length=20)),
                ('numfri', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack_id', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstallLengthBase',
            fields=[
                ('installlengthbase_id', models.AutoField(serialize=False, primary_key=True)),
                ('lineclasses_id', models.CharField(max_length=20)),
                ('diameter_id', models.CharField(max_length=20)),
                ('installlength', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack_id', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manhoursfactor',
            fields=[
                ('manhoursfactor_id', models.AutoField(serialize=False, primary_key=True)),
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
                ('numcoldcutsbase_id', models.AutoField(serialize=False, primary_key=True)),
                ('lineclasses_id', models.CharField(max_length=20)),
                ('diameter_id', models.CharField(max_length=20)),
                ('numcoldcuts', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack_id', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumberOfHotCutsBase',
            fields=[
                ('numhotcutsbase_id', models.AutoField(serialize=False, primary_key=True)),
                ('lineclasses_id', models.CharField(max_length=20)),
                ('diameter_id', models.CharField(max_length=20)),
                ('numhotcuts', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack_id', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumberOfJointsBase',
            fields=[
                ('numjointsbase_id', models.AutoField(serialize=False, primary_key=True)),
                ('lineclasses_id', models.CharField(max_length=20)),
                ('diameter_id', models.CharField(max_length=20)),
                ('numjoints', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workpack_id', models.ForeignKey(to='workpacks.Workpack', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pipingnorms',
            fields=[
                ('pipingnorms_id', models.AutoField(serialize=False, primary_key=True)),
                ('pipediameter', models.CharField(max_length=5)),
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
    ]
