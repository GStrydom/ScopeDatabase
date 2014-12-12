from __future__ import unicode_literals
from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return self.name