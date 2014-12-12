from django.db import models


class MatList(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class SizeList(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name