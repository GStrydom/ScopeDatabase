from django.db import models
from customers.models import Customer


class Project(models.Model):
    name = models.CharField(max_length=50, blank=True)
    datecreated = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.name