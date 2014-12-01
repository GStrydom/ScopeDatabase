from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext

from .forms import CreateNewPrefabForm

from workpacks.models import Lineclass, Workpack
from prefabrication.models import Prefabrication


def createprefabmatlist(request):
    """
    Create a new prefabrication material item tied to the workpack.
    """
    createprefabcons = dict()
    createprefabcons['newprefab'] = CreateNewPrefabForm(data=request.POST)
    createprefabcons['newprefab'].fields['matlist'].queryset = Lineclass.objects\
        .filter(lineclassname=Workpack.objects.get(workpack_id=request.session['workpackselected']).workpacklineclass)\
        .values_list('itemname', flat=True).distinct()

    if request.method == 'POST':
        if createprefabcons['newprefab'].is_valid():
            item = Lineclass.objects.get(itemname__icontains=createprefabcons['newprefab'].cleaned_data['matlist'],
                                         dn1__icontains=createprefabcons['newprefab'].cleaned_data['sizelist'],
                                         lineclassname__icontains=createprefabcons['newprefab']
                                         .cleaned_data['lineclasses'])

            savedform = createprefabcons['newprefab'].save()
            savedform.code = item.code
            savedform.save()
            return HttpResponseRedirect('/')

    createprefabcons['workpacks'] = Workpack.objects.all()

    return render_to_response('newprefab.html', createprefabcons, context_instance=RequestContext(request))


def editprefabitem(request, prefabrication_id):
    editcons = dict()
    editcons['prefab'] = Prefabrication.objects.get(prefabrication_id=prefabrication_id)
    editcons['editprefabform'] = CreateNewPrefabForm(request.POST or None, instance=editcons['prefab'])
    if editcons['editprefabform'].is_valid():
        editcons['editprefabform'].save()
        return HttpResponseRedirect('/')
    editcons['workpacks'] = Workpack.objects.all()

    return render_to_response('editprefab.html', editcons, context_instance=RequestContext(request))