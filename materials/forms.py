from django import forms

from .models import MaterialItem


class CreateNewMaterialForm(forms.ModelForm):

    class Meta:
        model = MaterialItem
        fields = ('lineclass', 'diameter', 'name', 'quantity')