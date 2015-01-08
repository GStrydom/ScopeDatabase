from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.db import User

from profiles.models import UserProfile

from .models import Workpack
from .classes import BaseWorkPack
from projects.models import Project

import datetime


def createworkpack(request):
    context = dict()
    context.update(csrf(request))
    if request.method == 'POST':
        workpack = BaseWorkPack(
            wrkpacknum=request.POST['addWorkpackNumberBox'],
            wrkpacklinenum=request.POST['addWorkpackLineNumberBox'],
            wrkpacklineclass=request.POST['addWorkpackLineclassBox'],
            wrkpackproject=request.POST['addWorkpackProjectBox'],
            wrkpacklead=User.objects.filter(username__exact=request.user.username),
            wrkpackzone=request.POST['addWorkpackZoneBox']
        )

        saved_workpack = Workpack(
            workpacknumber=workpack.workpacknumber,
            workpacklinenumber=workpack.workpacklinenumber,
            workpacklineclass=workpack.workpacklineclass,
            datecreated=datetime.datetime.today(),
            client=UserProfile.objects.filter(username__exact=request.user.username).company,
            lead=workpack.workpacklead,
            project=workpack.workpackproject,
            zone=workpack.workpackzone
        )

        saved_workpack.save()
        return HttpResponseRedirect('/home/')

    return render_to_response('addworkpack.html', context, context_instance=RequestContext(request))


def showworkpack(request, workpack_id):
    context = dict()
    context['workpack'] = Workpack.objects.get(id=workpack_id)
    request.session['workpackselected'] = context['workpack'].id

    return render_to_response('index.html', context, context_instance=RequestContext(request))


def editworkpack(request, workpack_id):
    context = dict()
    context['workpack'] = Workpack.objects.get(id=workpack_id)
    return render_to_response('editworkpack.html', context, context_instance=RequestContext(request))


def deletepack(request):
    deletecons = dict()
    workpack = Workpack.objects.get(workpack_id=request.session['workpackselected'])
    workpack.delete()
    deletecons['workpacks'] = Workpack.objects.all()

    return HttpResponseRedirect('/')