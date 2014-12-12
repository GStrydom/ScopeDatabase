from django.db import models


class Customerinformation(models.Model):
    contactnumber = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)


class Customer(models.Model):
    name = models.CharField(max_length=30, blank=True)
    datecreated = models.DateField(blank=True, null=True)
    customerinformation = models.ForeignKey(Customerinformation, blank=True, null=True)