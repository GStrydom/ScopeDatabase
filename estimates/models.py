from django.db import models

from workpacks.models import Workpack


class Manhoursfactor(models.Model):
    material = models.CharField(max_length=30, blank=True)
    pfitter = models.FloatField(blank=True, null=True)
    welder = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.manhoursfactor


class Pipingnorms(models.Model):
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
    duration_w_alkyfactor = models.FloatField(blank=True, null=True)
    cuttingfactorhacksaw = models.FloatField(blank=True, null=True)
    duration_w_hacksawfactor = models.FloatField(blank=True, null=True)
    fam_bafactor = models.FloatField(blank=True, null=True)
    duration_w_fam_bafactor = models.FloatField(blank=True, null=True)


class FieldWeldsBase(models.Model):
    lineclasses = models.CharField(max_length=20)
    diameter = models.FloatField()
    numberoffieldwelds = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    workpack = models.ForeignKey(Workpack, null=True)

    def __unicode__(self):
        return self.lineclasses + ' ' + self.workpack.workpacknumber


class DemoLengthBase(models.Model):
    lineclasses = models.CharField(max_length=20)
    diameter = models.CharField(max_length=20)
    demolength = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack = models.ForeignKey(Workpack, null=True)

    def __unicode__(self):
        return self.lineclasses


class InstallLengthBase(models.Model):
    lineclasses = models.CharField(max_length=20)
    diameter = models.CharField(max_length=20)
    installlength = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack = models.ForeignKey(Workpack, null=True)

    def __unicode__(self):
        return self.lineclasses


class FlangePressureTestBase(models.Model):
    lineclasses = models.CharField(max_length=20)
    diameter = models.CharField(max_length=20)
    numfpt = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack = models.ForeignKey(Workpack, null=True)
    flangehndlehotcut = models.BooleanField(default=False)
    alkybandc = models.BooleanField(default=False)
    hacksawcutting = models.BooleanField(default=False)
    fambaset = models.BooleanField(default=False)

    def __unicode__(self):
        return self.lineclasses


class FlangeReinstateBase(models.Model):
    lineclasses = models.CharField(max_length=20)
    diameter = models.CharField(max_length=20)
    numfri = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack = models.ForeignKey(Workpack, null=True)
    alkybandc = models.BooleanField(default=False)
    fambaset = models.BooleanField(default=False)

    def __unicode__(self):
        return self.lineclasses


class NumberOfJointsBase(models.Model):
    lineclasses = models.CharField(max_length=20)
    diameter = models.CharField(max_length=20)
    numjoints = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack = models.ForeignKey(Workpack, null=True)
    rigforjoints = models.BooleanField(default=False)
    instrumentsboltup = models.BooleanField(default=False)

    def __unicode__(self):
        return self.lineclasses


class NumberOfColdCutsBase(models.Model):
    lineclasses = models.CharField(max_length=20)
    diameter = models.CharField(max_length=20)
    numcoldcuts = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack = models.ForeignKey(Workpack, null=True)
    rigforcoldcut = models.BooleanField(default=False)

    def __unicode__(self):
        return self.lineclasses


class NumberOfHotCutsBase(models.Model):
    lineclasses = models.CharField(max_length=20)
    diameter = models.CharField(max_length=20)
    numhotcuts = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workpack = models.ForeignKey(Workpack, null=True)
    rigforhotcut = models.BooleanField(default=False)

    def __unicode__(self):
        return self.lineclasses