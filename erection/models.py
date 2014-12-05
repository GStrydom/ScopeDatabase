from __future__ import unicode_literals
from django.db import models


from workpacks.models import Workpack, Lineclass


class Erection(models.Model):
    erection_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    size = models.CharField(max_length=30, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    workpack = models.ForeignKey(Workpack, blank=True, null=True)
    lineclass = models.ForeignKey(Lineclass, blank=True, null=True)