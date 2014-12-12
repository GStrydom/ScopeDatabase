from django import forms

from .models import Spading


class CreateSpadingForm(forms.ModelForm):
    class Meta:
        model = Spading
        fields = ('matlist', 'sizelist', 'quantity', 'workpack', 'lineclasses')