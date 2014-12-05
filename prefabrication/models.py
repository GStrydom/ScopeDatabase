from __future__ import unicode_literals
from django.db import models

from workpacks.models import Workpack, Lineclasses


class Prefabrication(models.Model):
    prefabrication_id = models.AutoField(primary_key=True)
    matlist = models.CharField(max_length=50, blank=True)
    sizelist = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    workpack = models.ForeignKey(Workpack, blank=True, null=True)
    code = models.CharField(max_length=50)
    lineclasses = models.ForeignKey(Lineclasses)