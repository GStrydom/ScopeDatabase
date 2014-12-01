from __future__ import unicode_literals
from django.db import models


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    datecreated = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'

    def __unicode__(self):
        return self.name