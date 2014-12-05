from __future__ import unicode_literals
from django.db import models

from clients.models import Client
from projects.models import Project
from areas.models import Area, Zone


class Lead(models.Model):
    lead_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    datecreated = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Workpack(models.Model):
    workpack_id = models.AutoField(primary_key=True)
    workpacknumber = models.CharField(unique=True, max_length=30, blank=True)
    workpacklineclass = models.CharField(max_length=30, blank=True)
    workpacklinenumber = models.CharField(max_length=30, blank=True)
    datecreated = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Client, blank=True, null=True)
    lead = models.ForeignKey(Lead, blank=True, null=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    area = models.ForeignKey(Area, blank=True, null=True)

    def __unicode__(self):
        return self.workpacknumber

    def get_absolute_url(self):
        return 'workpack_detail_view', (), {'slug': self.slug}


class Lineclass(models.Model):
    lineclass_id = models.AutoField(primary_key=True)
    lineclassname = models.CharField(max_length=10, blank=True)
    itemname = models.CharField(max_length=30, blank=True)
    itemid = models.CharField(max_length=10, blank=True)
    material = models.CharField(max_length=20, blank=True)
    dn1 = models.CharField(max_length=20, blank=True)
    dn2 = models.CharField(max_length=20, blank=True)
    code = models.CharField(max_length=30, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True)
    bulkquantity = models.IntegerField(blank=True, null=True)
    bomunit = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.lineclassname


class Lineclasses(models.Model):
    lineclasses_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name