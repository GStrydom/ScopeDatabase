from __future__ import unicode_literals
from django.db import models

from workpacks.models import Workpack, Lineclasses
from materials.models import MatList, SizeList


class Reinstatement(models.Model):
    reinstatement_id = models.AutoField(primary_key=True)
    matlist = models.ForeignKey(MatList, blank=True, null=True)
    sizelist = models.ForeignKey(SizeList, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    workpack = models.ForeignKey(Workpack, blank=True, null=True)
    lineclasses = models.ForeignKey(Lineclasses, blank=True, null=True)