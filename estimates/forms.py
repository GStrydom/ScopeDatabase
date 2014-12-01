from django import forms

from .models import Estimate, EstimateDefaults


class NewEstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = ('estimate_id', 'manhours', 'duration', 'resources', 'name', 'workpack')


class NewDefaultEstimates(forms.ModelForm):
    class Meta:
        model = EstimateDefaults
        fields = ('estimatedefaults_id', 'lineclasses', 'diameter', 'schedule', 'material', 'fieldwelds',
                  'demolength', 'installlength', 'flangesforisolation', 'flangesforreinstate',
                  'flangehandlinghotcuts', 'flangehandlingalky', 'flangehandlinghacksaw', 'flangehandlingbaset',
                  'numberofjoints', 'instrumentsforboltup', 'riggersforboltup', 'numberofcoldcuts',
                  'numberofhotcuts', 'workpack')
        exclude = ('datecreated',)