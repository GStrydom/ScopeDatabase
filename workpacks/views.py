from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

from .forms import CreateWorkPackForm, EditWorkPackForm
from .models import Workpack


def createworkpack(request):
    createwpcons = dict()

    createwpcons['newwpform'] = CreateWorkPackForm(data=request.POST)

    if request.method == 'POST':
        if createwpcons['newwpform'].is_valid():
            createwpcons['newwpform'].save()

    createwpcons['workpacks'] = Workpack.objects.all()

    return render_to_response('new.html', createwpcons, context_instance=RequestContext(request))


def showworkpack(request, workpack_id):
    showpcons = dict()
    showpcons['workpack'] = Workpack.objects.get(id=workpack_id)
    request.session['workpackselected'] = showpcons['workpack'].id
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