from django import forms

from .models import MaterialItem
from workpacks.models import Lineclass
from estimates.models import Pipingnorms


class CreateNewMaterialForm(forms.ModelForm):
    lineclass = forms.ModelChoiceField(queryset=Lineclass.objects.values_list('itemname', flat=True).distinct())
    diameter = forms.ModelChoiceField(queryset=Pipingnorms.objects.values_list('dn', flat=True))

    class Meta:
        model = MaterialItem
        fields = ('lineclass', 'diameter', 'quantity', 'workpack', 'code')