from django import forms

from .models import Reinstatement


class CreateNewReinstateForm(forms.ModelForm):

    class Meta:
        model = Reinstatement
        fields = ('reinstatement_id', 'matlist', 'sizelist', 'quantity', 'workpack', 'lineclasses')