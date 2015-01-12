from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from workpacks.models import Workpack
from materials.models import MaterialItem, Lineclass11011, Lineclass11071

from .classes import BasePrefabItem, BaseReinstateItem, BaseSpadingItem

import datetime
import json as simplejson

from django.core import serializers


def showprefabitems(request):
    context = dict()

    context['materialitems'] = MaterialItem.objects.filter(type__exact='Prefabrica')\
        .filter(workpack_id__exact=request.session['workpackselected'])

    context['workpacks'] = Workpack.objects.all()

    return render_to_response('prefab.html', context, context_instance=RequestContext(request))


def getprefabnames(request):
    context = dict()

    return render_to_response('getprefabdiameter.html', context, context_instance=RequestContext(request))


def createprefabitem(request):
    context = dict()

    if request.method == 'POST':
        if 'lineclassSelected' in request.POST:
            request.session['prefabLineclassSelected'] = request.POST['lineclassSelected']

            return render_to_response('getprefabdiameter.html', context, context_instance=RequestContext(request))

    return render_to_response('addprefab.html', context, context_instance=RequestContext(request))


def editprefabitem(request, materialitem_id):
    context = dict()
    context['matitem'] = MaterialItem.objects.get(id=materialitem_id)
    context['workpacks'] = Workpack.objects.all()

    return render_to_response('addprefab.html', context, context_instance=RequestContext(request))


def deleteprefabitem(request):
    context = dict()
    return render_to_response('prefab.html', context, context_instance=RequestContext(request))


def showreinstateitems(request):
    context = dict()
    context['reinstates'] = MaterialItem.objects.filter(type__exact='Reinstatement')
    context['workpacks'] = Workpack.objects.all()
    return render_to_response('reinstate.html', context, context_instance=RequestContext(request))


def createreinstateitem(request):
    """
    Create a new materials material item tied to the workpack.
    """
    context = dict()

    if request.method == 'POST':
        if 'lineclass' in request.POST:
            item = BaseReinstateItem(
                lineclass=request.POST['reinstateLineclassCombo'],
                diameter=request.POST['reinstateLineclassCombo'],
                name=request.POST['reinstateNameCombo'],
                quantity=request.POST['reinstateQuantityBox']
            )
            saved_item = MaterialItem(
                name=item.name,
                type='Reinstatement',
                lineclass=item.lineclass,
                diameter=item.diameter,
                quantity=item.quantity,
                datecreated=datetime.datetime.today(),
                createdby=request.user.username,
                code=item.get_code(item.lineclass)
            )
            saved_item.save()
        else:
            pass
    context['lineclass11011'] = Lineclass11011.objects.values_list('itemname', flat=True).distinct

    return render_to_response('addreinstate.html', context, context_instance=RequestContext(request))


def editreinstateitem(request, materialitem_id):
    context = dict()
    context['matitem'] = MaterialItem.objects.get(id=materialitem_id)
    context['workpacks'] = Workpack.objects.all()

    return render_to_response('reinstate.html', context, context_instance=RequestContext(request))


def deletereinstateitem(request):
    context = dict()
    return render_to_response('reinstate.html', context, context_instance=RequestContext(request))


def showspadingitems(request):
    context = dict()
    context['spadings'] = MaterialItem.objects.filter(type__exact='Spading')
    return render_to_response('spading.html', context, context_instance=RequestContext(request))


def createspadingitem(request):
    """
    Create a new materials material item tied to the workpack.
    """
    context = dict()

    if request.method == 'POST':
        if 'lineclass' in request.POST:
            item = BaseSpadingItem(
                lineclass=request.POST['spadingLineclassCombo'],
                diameter=request.POST['spadingLineclassCombo'],
                name=request.POST['spadingNameCombo'],
                quantity=request.POST['spadingQuantityBox']
            )
            saved_item = MaterialItem(
                name=item.name,
                type='Spading',
                lineclass=item.lineclass,
                diameter=item.diameter,
                quantity=item.quantity,
                workpack=item.attach_to_workpack(),
                datecreated=datetime.datetime.today(),
                createdby=request.user.username
            )
            saved_item.save()
        else:
            pass

    return render_to_response('spading.html', context, context_instance=RequestContext(request))


def editspadingitem(request, materialitem_id):
    context = dict()
    context['matitem'] = MaterialItem.objects.get(id=materialitem_id)
    context['workpacks'] = Workpack.objects.all()

    return render_to_response('spading.html', context, context_instance=RequestContext(request))


def deletespadingitem(request):
    context = dict()
    return render_to_response('spading.html', context, context_instance=RequestContext(request))



    # if 'lineclass' in request.POST:
    #     item = BasePrefabItem(
    #         lineclass=request.POST['addPrefabLineclassBox'],
    #         diameter=request.POST['addPrefabDiameterBox'],
    #         name=request.POST['addPrefabNameBox'],
    #         quantity=request.POST['addPrefabQuantityBox']
    #     )
    #     saved_item = MaterialItem(
    #         name=item.name,
    #         type='Prefabrication',
    #         lineclass=item.lineclass,
    #         diameter=item.diameter,
    #         quantity=item.quantity,
    #         workpack=request.session['workpackselected'],
    #         datecreated=datetime.datetime.today(),
    #         createdby=request.user.username,
    #         code=item.get_code(item.lineclass)
    #     )
    #     saved_item.save()