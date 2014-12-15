from django.db import models

from workpacks.models import Workpack, Lead


class MaterialItem(models.Model):
    lineclass11011 = 11011,
    lineclass11071 = 11011,
    lineclass11261 = 11261,
    lineclass31011 = 31011,
    lineclass31071 = 31071,
    lineclass31261 = 31261

    lineclasses = (
        (lineclass11011, 11011),
        (lineclass11071, 11071),
        (lineclass11261, 11261),
        (lineclass31011, 31011),
        (lineclass31071, 31071),
        (lineclass31261, 31261)
    )
    name = models.CharField(max_length=10, blank=True, null=True)
    lineclass = models.CharField(max_length=10, choices=lineclasses, blank=True, null=True)
    diameter = models.CharField(max_length=5, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    workpack = models.ForeignKey(Workpack, blank=True, null=True)
    code = models.CharField(max_length=20)
    datecreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    createdby = models.ForeignKey(Lead, blank=True, null=True)