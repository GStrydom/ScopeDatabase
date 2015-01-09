from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

from profiles.models import UserProfile

from .models import Workpack
from .classes import BaseWorkPack

from django.contrib.auth.models import User

import datetime


def createworkpack(request):
    context = dict()
    context.update(csrf(request))
    context['usersname'] = request.user.username
    if request.method == 'POST':
        workpack = BaseWorkPack(
            wrkpacknum=request.POST['addWorkpackNumberBox'],
            wrkpacklinenum=request.POST['addWorkpackLineNumberBox'],
            wrkpacklineclass=request.POST['addWorkpackLineclassBox'],
            wrkpackproject=request.POST['addWorkpackProjectBox'],
            wrkpackzone=request.POST['addWorkpackZoneBox'],
            wrkpacklead=request.POST['addWorkpackLeadBox']
        )

        username = User.objects.filter(username__exact=request.user.username)
        user = UserProfile.objects.filter(user__exact=request.user)
        users = UserProfile.objects.all()
        print user

        saved_workpack = Workpack(
            workpacknumber=workpack.workpacknumber,
            workpacklinenumber=workpack.workpacklinenumber,
            workpacklineclass=workpack.workpacklineclass,
            datecreated=datetime.datetime.today(),
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

    return render_to_response('workpackinfo.html', context, context_instance=RequestContext(request))


def editworkpack(request, workpack_id):
    context = dict()
    context.update(csrf(request))
    context['workpack'] = Workpack.objects.get(id=workpack_id)

    if request.method == 'POST':
        if 'editWorkpackNumberBox' in request.POST:
            context['workpack'].workpacknumber = request.POST['editWorkpackNumberBox']
            context['workpack'].workpacklinenumber = request.POST['editWorkpackLineNumberBox']
            context['workpack'].workpacklineclass = request.POST['editWorkpackLineclassBox']
            context['workpack'].project = request.POST['editWorkpackProjectBox']
            context['workpack'].lead = request.POST['editWorkpackLeadBox']
            context['workpack'].workpackzone = request.POST['editWorkpackZoneBox']
            context['workpack'].save()
    HttpResponseRedirect('/home/')

    return render_to_response('editworkpack.html', context, context_instance=RequestContext(request))


def deletepack(request):
    workpack = Workpack.objects.get(id=request.session['workpackselected'])
    workpack.delete()
    return HttpResponseRedirect('/home/')