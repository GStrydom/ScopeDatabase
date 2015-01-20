from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required

from workpacks.models import Workpack


@login_required(login_url='/')
def homepageview(request):
    context = dict()
    context.update(csrf(request))
    context['workpacks'] = Workpack.objects.all()

    groups = models.Group.objects.get(name='Admins')
    admin_users = groups.user_set.all()

    for users in admin_users:
        if request.user.username in users.username:
            context['adminuser'] = 1
        else:
            context['adminuser'] = 0

    return render_to_response('index.html', context, context_instance=RequestContext(request))


def exportbom(request):

    return HttpResponseRedirect('/home/')


@login_required(login_url='/')
def userslist(request):
    context = dict()

    groups = models.Group.objects.get(name='Admins')
    admin_users = groups.user_set.all()

    for users in admin_users:
        if request.user.username in users.username:
            context['adminuser'] = 1
        else:
            context['adminuser'] = 0

    return render_to_response('users.html', context, context_instance=RequestContext(request))