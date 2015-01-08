from django.db import models

from clients.models import Client
from projects.models import Project
from areas.models import Zone


class Lead(models.Model):
    name = models.CharField(max_length=50, blank=True)
    datecreated = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Workpack(models.Model):
    workpacknumber = models.CharField(unique=True, max_length=30, blank=True, null=True)
    workpacklineclass = models.CharField(max_length=30, blank=True, null=True)
    workpacklinenumber = models.CharField(max_length=30, blank=True, null=True)
    datecreated = models.DateField(blank=True, null=True)
    lead = models.CharField(max_length=50, blank=True, null=True)
    project = models.CharField(max_length=30, blank=True, null=True)
    zone = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.workpacknumber