from django import forms

from .models import FieldWeldsBase
from .models import DemoLengthBase, InstallLengthBase, FlangePressureTestBase, FlangeReinstateBase
from .models import NumberOfJointsBase, NumberOfColdCutsBase, NumberOfHotCutsBase


class FieldWeldsBaseForm(forms.ModelForm):

    class Meta:
        model = FieldWeldsBase
        fields = ('lineclasses', 'diameter', 'numberoffieldwelds', 'workpack')
        exclude = ('workpack',)


class DemoLengthBaseForm(forms.ModelForm):

    class Meta:
        model = DemoLengthBase
        fields = ('lineclasses', 'diameter', 'demolength', 'workpack')


class InstallLengthBaseForm(forms.ModelForm):

    class Meta:
        model = InstallLengthBase
        fields = ('lineclasses', 'diameter', 'installlength', 'workpack')


class FlangePressureTestBaseForm(forms.ModelForm):

    class Meta:
        model = FlangePressureTestBase
        fields = ('lineclasses', 'diameter', 'numfpt', 'workpack', 'flangehndlehotcut', 'alkybandc', 'hacksawcutting',
                  'fambaset')


class FlangeReinstateBaseForm(forms.ModelForm):

    class Meta:
        model = FlangeReinstateBase
        fields = ('lineclasses', 'diameter', 'numfri', 'workpack', 'alkybandc', 'fambaset')


class NumberOfJointsBaseForm(forms.ModelForm):

    class Meta:
        model = NumberOfJointsBase
        fields = ('lineclasses', 'diameter', 'numjoints', 'workpack', 'rigforjoints', 'instrumentsboltup')


class NumberOfColdCutsBaseForm(forms.ModelForm):

    class Meta:
        model = NumberOfColdCutsBase
        fields = ('lineclasses', 'diameter', 'numcoldcuts', 'workpack')


class NumberOfHotCutsBaseForm(forms.ModelForm):

    class Meta:
        model = NumberOfHotCutsBase
        fields = ('lineclasses', 'diameter', 'numhotcuts', 'workpack')