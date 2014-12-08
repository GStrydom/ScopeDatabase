from django.db import models

from datetime import datetime

from workpacks.models import Workpack, Lineclasses, Lineclass

from materials.models import SizeList

from django.db.models.signals import pre_delete
from django.dispatch import receiver


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

    def __unicode__(self):
        return self.manhoursfactor_id


class Pipingnorms(models.Model):
    """
    Lookup tables for estimates.
    """
    pipingnorms_id = models.AutoField(primary_key=True)
    pipediameter = models.FloatField()
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


class SpadingNorms(models.Model):
    sizes = models.FloatField(blank=True, null=True)
    manhrs = models.FloatField(blank=True, null=True)
    res = models.FloatField(blank=True, null=True)
    durtopenclose = models.FloatField(blank=True, null=True)
    cuttingfactorhw = models.FloatField(blank=True, null=True)
    durationhwfactor = models.FloatField(blank=True, null=True)
    alkyfactor_b_and_c_class = models.FloatField(blank=True, null=True)
    duration_w_alkyfactor = models.FloatField(blank=True,null=True)
    cuttingfactorhacksaw = models.FloatField(blank=True, null=True)
    duration_w_hacksawfactor = models.FloatField(blank=True, null=True)
    fam_bafactor = models.FloatField(blank=True, null=True)
    duration_w_fam_bafactor = models.FloatField(blank=True, null=True)


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


class FieldWeldsBase(models.Model):
    fieldweld_id = models.AutoField(primary_key=True)
    lineclasses_id = models.CharField(max_length=20)
    diameter_id = models.FloatField()
    numberoffieldwelds = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    workpack_id = models.ForeignKey(Workpack, null=True)

    def __unicode__(self):
        return self.lineclasses_id


class FieldWeldsHours(models.Model):
    fieldweldshours_id = models.AutoField(primary_key=True)
    resources = models.SmallIntegerField(blank=True)
    manhours = models.FloatField(blank=True)
    duration = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    fieldweldbase = models.ForeignKey(FieldWeldsBase, blank=True, null=True)

    def __unicode__(self):
        return self


class DemoLengthBase(models.Model):
    demolengthbase_id = models.AutoField(primary_key=True)
    lineclasses_id = models.CharField(max_length=20)
    diameter_id = models.CharField(max_length=20)
    demolength = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack_id = models.ForeignKey(Workpack, null=True)

    def __unicode__(self):
        return self.lineclasses_id


class DemoLengthHours(models.Model):
    demolengthhours_id = models.AutoField(primary_key=True)
    resources = models.SmallIntegerField(blank=True)
    manhours = models.FloatField(blank=True)
    duration = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    workpack_id = models.ForeignKey(Workpack, null=True)

    def __unicode__(self):
        return self.resources


class InstallLengthBase(models.Model):
    installlengthbase_id = models.AutoField(primary_key=True)
    lineclasses_id = models.CharField(max_length=20)
    diameter_id = models.CharField(max_length=20)
    installlength = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack_id = models.ForeignKey(Workpack, null=True)

    def __unicode__(self):
        return self.lineclasses_id


class FlangePressureTestBase(models.Model):
    fptbase_id = models.AutoField(primary_key=True)
    lineclasses_id = models.CharField(max_length=20)
    diameter_id = models.CharField(max_length=20)
    numfpt = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack_id = models.ForeignKey(Workpack, null=True)
    flangehndlehotcut = models.BooleanField(default=False)
    alkybandc = models.BooleanField(default=False)
    hacksawcutting = models.BooleanField(default=False)
    fambaset = models.BooleanField(default=False)

    def __unicode__(self):
        return self.lineclasses_id


class FlangeReinstateBase(models.Model):
    fribase_id = models.AutoField(primary_key=True)
    lineclasses_id = models.CharField(max_length=20)
    diameter_id = models.CharField(max_length=20)
    numfri = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack_id = models.ForeignKey(Workpack, null=True)
    alkybandc = models.BooleanField(default=False)
    fambaset = models.BooleanField(default=False)

    def __unicode__(self):
        return self.lineclasses_id


class NumberOfJointsBase(models.Model):
    numjointsbase_id = models.AutoField(primary_key=True)
    lineclasses_id = models.CharField(max_length=20)
    diameter_id = models.CharField(max_length=20)
    numjoints = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack_id = models.ForeignKey(Workpack, null=True)
    rigforjoints = models.BooleanField(default=False)
    instrumentsboltup = models.BooleanField(default=False)

    def __unicode__(self):
        return self.lineclasses_id


class NumberOfColdCutsBase(models.Model):
    numcoldcutsbase_id = models.AutoField(primary_key=True)
    lineclasses_id = models.CharField(max_length=20)
    diameter_id = models.CharField(max_length=20)
    numcoldcuts = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack_id = models.ForeignKey(Workpack, null=True)

    def __unicode__(self):
        return self.lineclasses_id


class NumberOfHotCutsBase(models.Model):
    numhotcutsbase_id = models.AutoField(primary_key=True)
    lineclasses_id = models.CharField(max_length=20)
    diameter_id = models.CharField(max_length=20)
    numhotcuts = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack_id = models.ForeignKey(Workpack, null=True)
    rigforhotcut = models.BooleanField(default=False)

    def __unicode__(self):
        return self.lineclasses_id