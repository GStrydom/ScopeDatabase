from django.db import models
from django.core.urlresolvers import reverse

from datetime import datetime

from workpacks.models import Workpack, Lineclasses, Lineclass

from materials.models import SizeList


class Estimate(models.Model):
    """
    Holds the values for the each estimate after calculations
    have been done.
    """
    estimate_id = models.AutoField(primary_key=True)
    manhours = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    resources = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255, blank=True)
    workpack = models.ForeignKey(Workpack, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estimate'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Manhoursfactor(models.Model):
    """
    Lookup table for estimates.
    """
    manhoursfactor_id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=30, blank=True)
    pfitter = models.FloatField(blank=True, null=True)
    welder = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manhoursfactor'

    def __unicode__(self):
        return self.manhoursfactor_id


class Pipingnorms(models.Model):
    """
    Lookup tables for estimates.
    """
    pipingnorms_id = models.AutoField(primary_key=True)
    pipediameter = models.CharField(max_length=5)
    handlemeternormshours = models.FloatField()
    hotcutnormhours = models.FloatField()
    coldcutnormhours = models.FloatField()
    boltupjointnormhours = models.FloatField()
    spadejointnormhours = models.FloatField()
    cut = models.FloatField()
    prep = models.FloatField()
    tackweldgreateighty = models.FloatField()
    tackweldlesseighty = models.FloatField()
    dn = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pipingnorms'

    def __unicode__(self):
        return self.pipingnorms_id


class EstimateDefaults(models.Model):
    """
    Preps EPDS with default duration/manhours ready for
    resources.
    """

    estimatedefaults_id = models.AutoField(primary_key=True)
    lineclasses = models.ForeignKey(Lineclasses)
    diameter = models.IntegerField()
    schedule = models.CharField(max_length=10, blank=True)
    material = models.CharField(max_length=10, blank=True)
    fieldwelds = models.SmallIntegerField(blank=True)
    demolength = models.SmallIntegerField(blank=True)
    installlength = models.SmallIntegerField(blank=True)
    flangesforisolation = models.SmallIntegerField(blank=True)
    flangesforreinstate = models.SmallIntegerField(blank=True)
    flangehandlinghotcuts = models.BooleanField(default=False)
    flangehandlingalky = models.BooleanField(default=False)
    flangehandlinghacksaw = models.BooleanField(default=False)
    flangehandlingbaset = models.BooleanField(default=False)
    numberofjoints = models.SmallIntegerField(blank=True)
    instrumentsforboltup = models.BooleanField(default=False)
    riggersforboltup = models.BooleanField(default=False)
    numberofcoldcuts = models.SmallIntegerField(blank=True)
    numberofhotcuts = models.SmallIntegerField(blank=True)
    workpack = models.ForeignKey(Workpack)
    datecreated = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'estimatedefaults'


class FieldWeldsBase(models.Model):
    fieldweld_id = models.AutoField(primary_key=True)
    lineclasses_id = models.CharField(max_length=20)
    diameter_id = models.CharField(max_length=20)
    numberoffieldwelds = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.created


class FieldWeldsHours(models.Model):
    fieldweldshours_id = models.AutoField(primary_key=True)
    resources = models.SmallIntegerField(blank=True)
    manhours = models.FloatField(blank=True)
    duration = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.created