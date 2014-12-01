from __future__ import unicode_literals
from django.db import models


class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'zone'

    def __unicode__(self):
        return self.name


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    zone = models.ForeignKey(Zone, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'

    def __unicode__(self):
        return self.name