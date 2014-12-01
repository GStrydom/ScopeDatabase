from __future__ import unicode_literals
from django.db import models

from workpacks.models import Workpack, Lineclasses
from materials.models import MatList, SizeList


class Prefabrication(models.Model):
    prefabrication_id = models.AutoField(primary_key=True)
    matlist = models.ForeignKey(MatList, blank=True, null=True)
    sizelist = models.ForeignKey(SizeList, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    workpack = models.ForeignKey(Workpack, blank=True, null=True)
    code = models.CharField(max_length=50)
    lineclasses = models.ForeignKey(Lineclasses)

    class Meta:
        managed = False
        db_table = 'prefabrication'