from django.db import models


class MatList(models.Model):
    matlist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class SizeList(models.Model):
    sizelist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name