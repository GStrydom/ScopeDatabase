from django import forms

from .models import Prefabrication
from workpacks.models import Lineclass
from estimates.models import Pipingnorms


class CreateNewPrefabForm(forms.ModelForm):
    matlist = forms.ModelChoiceField(queryset=Lineclass.objects.values_list(u'itemname', flat=True).distinct())
    sizelist = forms.ModelChoiceField(queryset=Pipingnorms.objects.values_list(u'dn', flat=True))

    class Meta:
        model = Prefabrication
        fields = ('matlist', 'sizelist', 'quantity', 'workpack', 'lineclasses')