from django import forms

from .models import Spading


class CreateSpadingForm(forms.ModelForm):
    class Meta:
        model = Spading
        fields = ('spading_id', 'matlist', 'sizelist', 'quantity', 'workpack', 'lineclasses')