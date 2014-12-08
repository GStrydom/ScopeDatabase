from django import forms

from .models import Workpack, Lineclass


class CreateWorkPackForm(forms.ModelForm):
    class Meta:
        model = Workpack
        fields = ('workpack_id', 'workpacknumber', 'workpacklinenumber', 'workpacklineclass', 'datecreated',
                  'lead', 'project', 'area')


class EditWorkPackForm(forms.ModelForm):
        class Meta:
            model = Workpack
            fields = ('workpack_id', 'workpacknumber', 'workpacklinenumber', 'workpacklineclass', 'datecreated',
                      'client', 'lead', 'project', 'area')