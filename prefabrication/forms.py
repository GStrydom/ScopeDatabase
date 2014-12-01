from django import forms

from .models import Prefabrication


class CreateNewPrefabForm(forms.ModelForm):

    class Meta:
        model = Prefabrication
        fields = ('prefabrication_id', 'matlist', 'sizelist', 'quantity', 'workpack', 'lineclasses')