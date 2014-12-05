from django.db import models


class Customerinformation(models.Model):
    customerinformation_id = models.AutoField(primary_key=True)
    contactnumber = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    datecreated = models.DateField(blank=True, null=True)
    customerinformation = models.ForeignKey(Customerinformation, blank=True, null=True)