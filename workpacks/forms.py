from django import forms

from .models import Workpack


class CreateWorkPackForm(forms.ModelForm):
    class Meta:
        model = Workpack
        fields = ('workpacknumber', 'workpacklinenumber', 'workpacklineclass', 'datecreated',
                  'lead', 'project', 'zone')


class EditWorkPackForm(forms.ModelForm):
        class Meta:
            model = Workpack
            fields = ('workpacknumber', 'workpacklinenumber', 'workpacklineclass', 'datecreated',
                      'client', 'lead', 'project', 'zone')