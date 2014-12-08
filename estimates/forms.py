from django import forms

from .models import Estimate, EstimateDefaults, Pipingnorms, FieldWeldsBase, Lineclass, Lineclasses, DemoLengthHours
from .models import FieldWeldsHours, DemoLengthBase, InstallLengthBase, FlangePressureTestBase, FlangeReinstateBase
from .models import NumberOfJointsBase, NumberOfColdCutsBase, NumberOfHotCutsBase


class NewEstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = ('estimate_id', 'manhours', 'duration', 'resources', 'name', 'workpack')


class NewDefaultEstimates(forms.ModelForm):
    diameter = forms.ModelChoiceField(queryset=Pipingnorms.objects.values_list('dn', flat=True))

    class Meta:
        model = EstimateDefaults
        fields = ('estimatedefaults_id', 'lineclasses', 'diameter', 'fieldwelds',
                  'demolength', 'installlength', 'flangesforisolation', 'flangesforreinstate',
                  'flangehandlinghotcuts', 'flangehandlingalky', 'flangehandlinghacksaw', 'flangehandlingbaset',
                  'numberofjoints', 'instrumentsforboltup', 'riggersforboltup', 'numberofcoldcuts',
                  'numberofhotcuts', 'workpack')
        exclude = ('datecreated',)


class FieldWeldsBaseForm(forms.ModelForm):

    class Meta:
        model = FieldWeldsBase
        fields = ('fieldweld_id', 'lineclasses_id', 'diameter_id', 'numberoffieldwelds', 'workpack_id')
        exclude = ('workpack_id',)


class FieldWeldHoursForm(forms.ModelForm):

    class Meta:
        model = FieldWeldsHours
        fields = ('fieldweldshours_id', 'resources', 'manhours', 'duration')


class DemoLengthHoursForm(forms.ModelForm):

    class Meta:
        model = DemoLengthHours
        fields = ('demolengthhours_id', 'resources', 'manhours', 'duration')


class DemoLengthBaseForm(forms.ModelForm):

    class Meta:
        model = DemoLengthBase
        fields = ('demolengthbase_id', 'lineclasses_id', 'diameter_id', 'demolength', 'workpack_id')


class InstallLengthBaseForm(forms.ModelForm):

    class Meta:
        model = InstallLengthBase
        fields = ('installlengthbase_id', 'lineclasses_id', 'diameter_id', 'installlength', 'workpack_id')


class FlangePressureTestBaseForm(forms.ModelForm):

    class Meta:
        model = FlangePressureTestBase
        fields = ('fptbase_id', 'lineclasses_id', 'diameter_id', 'numfpt', 'workpack_id', 'flangehndlehotcut', 'alkybandc', 'hacksawcutting', 'fambaset')


class FlangeReinstateBaseForm(forms.ModelForm):

    class Meta:
        model = FlangeReinstateBase
        fields = ('fribase_id', 'lineclasses_id', 'diameter_id', 'numfri', 'workpack_id', 'alkybandc', 'fambaset')


class NumberOfJointsBaseForm(forms.ModelForm):

    class Meta:
        model = NumberOfJointsBase
        fields = ('numjointsbase_id', 'lineclasses_id', 'diameter_id', 'numjoints', 'workpack_id', 'rigforjoints', 'instrumentsboltup')


class NumberOfColdCutsBaseForm(forms.ModelForm):

    class Meta:
        model = NumberOfColdCutsBase
        fields = ('numcoldcutsbase_id', 'lineclasses_id', 'diameter_id', 'numcoldcuts', 'workpack_id')


class NumberOfHotCutsBaseForm(forms.ModelForm):

    class Meta:
        model = NumberOfHotCutsBase
        fields = ('numhotcutsbase_id', 'lineclasses_id', 'diameter_id', 'numhotcuts', 'workpack_id')