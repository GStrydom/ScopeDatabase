from __future__ import unicode_literals
from django.db import models

from workpacks.models import Workpack, Lineclasses
from materials.models import MatList, SizeList


class Spading(models.Model):
    spading_id = models.AutoField(primary_key=True)
    matlist = models.ForeignKey(MatList)
    sizelist = models.ForeignKey(SizeList)
    quantity = models.IntegerField(blank=True, null=True)
    workpack = models.ForeignKey(Workpack, blank=True, null=True)
    lineclasses = models.ForeignKey(Lineclasses, blank=True, null=True)
    code = models.CharField(max_length=50)