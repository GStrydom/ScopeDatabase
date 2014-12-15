from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext

from .forms import CreateNewMaterialForm

from workpacks.models import Lineclass, Workpack
from materials.models import MaterialItem


def creatematerialitem(request):
    """
    Create a new materials material item tied to the workpack.
    """
    context = dict()
    context['newprefab'] = CreateNewMaterialForm(data=request.POST)
    context['newprefab'].fields['matlist'].queryset = Lineclass.objects\
        .filter(lineclassname=Workpack.objects.get(workpack_id=request.session['workpackselected']).workpacklineclass)\
        .values_list('itemname', flat=True).distinct()

    if request.method == 'POST':
        if context['newprefab'].is_valid():
            item = Lineclass.objects.get(itemname__icontains=context['newprefab'].cleaned_data['matlist'],
                                         dn1__icontains=context['newprefab'].cleaned_data['sizelist'],
                                         lineclassname__icontains=context['newprefab']
                                         .cleaned_data['lineclass'])

            savedform = context['newprefab'].save()
            savedform.code = item.code
            savedform.save()
            return HttpResponseRedirect('/')

    context['workpacks'] = Workpack.objects.all()

    return render_to_response('newprefab.html', context, context_instance=RequestContext(request))


def editmaterialitem(request, materialitem_id):
    context = dict()
    context['matitem'] = MaterialItem.objects.get(id=materialitem_id)
    context['editmaterialform'] = CreateNewMaterialForm(request.POST or None, instance=context['matitem'])
    if context['editmaterialform'].is_valid():
        context['editmaterialform'].save()
        return HttpResponseRedirect('/')
    context['workpacks'] = Workpack.objects.all()

    return render_to_response('editprefab.html', context, context_instance=RequestContext(request))