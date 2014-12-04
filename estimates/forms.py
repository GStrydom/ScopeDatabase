from django import forms

from .models import Estimate, EstimateDefaults, Pipingnorms, FieldWeldsBase, Lineclass, Lineclasses, DemoLengthHours
from .models import FieldWeldsHours, DemoLengthBase


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
        fields = ('fieldweld_id', 'lineclasses_id', 'diameter_id', 'numberoffieldwelds', 'workpack')
        exclude = ('workpack',)


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
        fields = ('demolengthbase_id', 'lineclasses_id', 'diameter_id', 'demolength')