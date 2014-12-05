from __future__ import unicode_literals
from django.db import models


class Clientinformation(models.Model):
    clientinformation_id = models.AutoField(primary_key=True)
    contactnumber = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    datecreated = models.DateField(blank=True, null=True)
    customerinformation = models.ForeignKey(Clientinformation, blank=True, null=True)

    def __unicode__(self):
        return self.name