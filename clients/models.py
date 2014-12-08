from django.db import models

from projects.models import Project


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    client_contactnumber = models.IntegerField(blank=True, null=True)
    client_email = models.CharField(max_length=50, blank=True, null=True)
    client_address = models.CharField(max_length=255, blank=True, null=True)
    client_project = models.ForeignKey(Project, null=True)
    datecreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '%s' % self.name