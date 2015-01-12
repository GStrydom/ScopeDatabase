from django import forms
from django.core.urlresolvers import reverse_lazy

from .models import MaterialItem

from clever_selects.form_fields import ChainedChoiceField
from clever_selects.forms import ChainedChoicesForm


class CreateNewPrefabItemForm(ChainedChoicesForm):
    lineclass = forms.ChoiceField(choices=(((11011, '11011'), (11071, '11071'), (11261, '11261'),
                                           (31011, '31011'), (31071, '31071'), (31261, '31261'))))
    name = ChainedChoiceField(parent_field='lineclass', ajax_url=reverse_lazy('createprefabitem'))