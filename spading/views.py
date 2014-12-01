from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

from .forms import CreateSpadingForm
from workpacks.models import Workpack, Lineclass
from .models import Spading


def createspadematlist(request):
    """
    Create a new prefabrication material item tied to the workpack.
    """
    createspadecons = dict()
    createspadecons['newspade'] = CreateSpadingForm(data=request.POST)

    if request.method == 'POST':
        if createspadecons['newspade'].is_valid():
            item = Lineclass.objects.get(itemname__icontains=createspadecons['newspade'].cleaned_data['matlist'],
                                         dn1__icontains=createspadecons['newspade'].cleaned_data['sizelist'],
                                         lineclassname__icontains=createspadecons['newspade'].cleaned_data['lineclasses'])

            savedform = createspadecons['newspade'].save()
            savedform.code = item.code
            savedform.save()
            return HttpResponseRedirect('/')

    createspadecons['workpacks'] = Workpack.objects.all()

    return render_to_response('newspade.html', createspadecons, context_instance=RequestContext(request))


def editspadeitem(request, spading_id):
    editcons = dict()
    editcons['spade'] = Spading.objects.get(spading_id=spading_id)
    editcons['editspadeform'] = CreateSpadingForm(request.POST or None, instance=editcons['spade'])
    if editcons['editspadeform'].is_valid():
        editcons['editspadeform'].save()
        return HttpResponseRedirect('/')
    editcons['workpacks'] = Workpack.objects.all()

    return render_to_response('editspade.html', editcons, context_instance=RequestContext(request))