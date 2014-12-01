from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

from .forms import CreateWorkPackForm, EditWorkPackForm
from .models import Workpack
from estimates.models import EstimateDefaults
from prefabrication.models import Prefabrication
from spading.models import Spading
from reinstatement.models import Reinstatement


def createworkpack(request):
    createwpcons = dict()

    createwpcons['newwpform'] = CreateWorkPackForm(data=request.POST)

    if request.method == 'POST':
        if createwpcons['newwpform'].is_valid():
            createwpcons['newwpform'].save()
            return HttpResponseRedirect('/')

    createwpcons['workpacks'] = Workpack.objects.all()

    return render_to_response('new.html', createwpcons, context_instance=RequestContext(request))


def showworkpack(request, workpack_id):
    showpcons = dict()
    showpcons['workpack'] = Workpack.objects.get(workpack_id=workpack_id)
    request.session['workpackselected'] = showpcons['workpack'].workpack_id
    showpcons['workpacks'] = Workpack.objects.all()
    return render_to_response('detail.html', showpcons, context_instance=RequestContext(request))


def editworkpack(request):
    editcons = dict()
    editcons['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
    editcons['editform'] = CreateWorkPackForm(request.POST or None, instance=editcons['workpack'])
    if editcons['editform'].is_valid():
        editcons['editform'].save()
        return HttpResponseRedirect('/')
    editcons['workpacks'] = Workpack.objects.all()
    return render_to_response('edit.html', editcons, context_instance=RequestContext(request))


def deletepack(request):
    deletecons = dict()
    workpack = Workpack.objects.get(workpack_id=request.session['workpackselected'])
    workpack.delete()
    deletecons['workpacks'] = Workpack.objects.all()
    return HttpResponseRedirect('/')


def showprefab(request):
    """
    Show all prefabrication items currently listed under the workpack.
    """
    showprefabcons = dict()
    showprefabcons['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
    showprefabcons['prefabs'] = Prefabrication.objects.select_related()\
                                            .filter(workpack_id=showprefabcons['workpack'].workpack_id)
    showprefabcons['workpacks'] = Workpack.objects.all()
    return render_to_response('showprefab.html', showprefabcons, context_instance=RequestContext(request))


def showspade(request):
    """
    Show all prefabrication items currently listed under the workpack.
    """
    showprefabcons = dict()
    showprefabcons['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
    showprefabcons['prefabs'] = Spading.objects.select_related()\
                                            .filter(workpack_id=showprefabcons['workpack'].workpack_id)
    showprefabcons['workpacks'] = Workpack.objects.all()
    return render_to_response('showspade.html', showprefabcons, context_instance=RequestContext(request))


def showreinstate(request):
    """
    Show all prefabrication items currently listed under the workpack.
    """
    showprefabcons = dict()
    showprefabcons['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
    showprefabcons['prefabs'] = Reinstatement.objects.select_related()\
                                            .filter(workpack_id=showprefabcons['workpack'].workpack_id)
    showprefabcons['workpacks'] = Workpack.objects.all()
    return render_to_response('showreinstate.html', showprefabcons, context_instance=RequestContext(request))