from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

from .models import Workpack

from .classes import BaseWorkPack


def createworkpack(request):
    context = dict()
    workpack = BaseWorkPack(
        wrkpacknum=request.POST['workpackNumber'],
        wrkpacklinenum=request.POST['workpackLineNumber'],
        wrkpacklineclass=request.POST['workpackLineclass'],
        wrkpackproject=request.POST['workpackProject'],
        wrkpacklead=request.POST['workpackLead'],
        wrkpackzone=request.POST['workpackZone']
    )

    saved_workpack = Workpack(
        workpacknumber=workpack.wrkpacknum
        workpacklineclass=workpack.wo
    )

    return render_to_response('addworkpack.html', context, context_instance=RequestContext(request))


def showworkpack(request, workpack_id):
    context = dict()
    context['workpack'] = Workpack.objects.get(id=workpack_id)
    request.session['workpackselected'] = context['workpack'].id

    return render_to_response('index.html', context, context_instance=RequestContext(request))


def editworkpack(request):
    editcons = dict()

    return render_to_response('editworkpack.html', editcons, context_instance=RequestContext(request))


def deletepack(request):
    deletecons = dict()
    workpack = Workpack.objects.get(workpack_id=request.session['workpackselected'])
    workpack.delete()
    deletecons['workpacks'] = Workpack.objects.all()

    return HttpResponseRedirect('/')