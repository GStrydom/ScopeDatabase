from django.db import models

from workpacks.models import Workpack, Lead

from smart_selects.db_fields import ChainedForeignKey


class Lineclass(models.Model):
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
        return self.itemname


class MaterialItem(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    lineclass = models.CharField(max_length=10, blank=True, null=True)
    diameter = models.CharField(max_length=5, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    workpack = models.ForeignKey(Workpack, blank=True, null=True)
    code = models.CharField(max_length=30)
    datecreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    createdby = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.name