from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from workpacks.models import Workpack
from materials.models import MaterialItem, Lineclass

import json
import datetime


@login_required(login_url='/')
def showprefabitems(request):
    context = dict()

    context['materialitems'] = MaterialItem.objects.filter(type__exact='Prefabrication')\
        .filter(workpack_id__exact=request.session['workpackselected'])

    return render_to_response('prefab.html', context, context_instance=RequestContext(request))


# Turns a ValuesQuerySet into dict objects...
def valuesquerysettodict(vqs):
    return [item for item in vqs]


@login_required(login_url='/')
def createprefabitem(request):
    context = dict()

    if request.method == 'POST':

        if 'lineclassSelected' in request.POST:
            lclass = Lineclass.objects.filter(lineclassname=request.POST['lineclassSelected'])\
                .values_list('itemname', flat=True).distinct()
            request.session['lineclassselected'] = request.POST['lineclassSelected']
            lineclass = valuesquerysettodict(lclass)
            return HttpResponse(json.dumps(lineclass), content_type='application/json')

        if 'itemSelected' in request.POST:
            item = Lineclass.objects.filter(itemname=request.POST['itemSelected'])[0]
            diams = Lineclass.objects.filter(itemname=item.itemname).values_list('dn1', flat=True).distinct()
            request.session['itemselected'] = request.POST['itemSelected']
            diameters = valuesquerysettodict(diams)
            return HttpResponse(json.dumps(diameters), content_type='application/json')

        if 'diamSelected' in request.POST:
            request.session['diameterselected'] = request.POST['diamSelected']

        if 'addPrefabQuantityBox' in request.POST:



            code = Lineclass.objects.filter(lineclassname=request.session['lineclassselected'])\
                .filter(itemname=request.session['itemselected']).filter(dn1=request.session['diameterselected'])[0]\
                .code
            request.session['prefabquantityselected'] = request.POST['addPrefabQuantityBox']



    return render_to_response('addprefab.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def editprefabitem(request, materialitem_id):
    context = dict()
    mat_item = MaterialItem.objects.get(id=materialitem_id)

    if request.method == 'POST':

        if 'lineclassSelected' in request.POST:
            lclass = Lineclass.objects.filter(lineclassname=request.POST['lineclassSelected'])\
                .values_list('itemname', flat=True).distinct()
            request.session['lineclassselected'] = request.POST['lineclassSelected']
            lineclass = valuesquerysettodict(lclass)
            return HttpResponse(json.dumps(lineclass), content_type='application/json')

        if 'itemSelected' in request.POST:
            item = Lineclass.objects.filter(itemname=request.POST['itemSelected'])[0]
            diams = Lineclass.objects.filter(itemname=item.itemname).values_list('dn1', flat=True).distinct()
            request.session['itemselected'] = request.POST['itemSelected']
            diameters = valuesquerysettodict(diams)
            return HttpResponse(json.dumps(diameters), content_type='application/json')

        if 'diamSelected' in request.POST:
            request.session['diameterselected'] = request.POST['diamSelected']

        if 'editPrefabQuantityBox' in request.POST:
            code = Lineclass.objects.filter(lineclassname=request.session['lineclassselected'])\
                .filter(itemname=request.session['itemselected']).filter(dn1=request.session['diameterselected'])[0]\
                .code

            mat_item.name = request.session['itemselected'],
            mat_item.type = 'Prefabrication',
            mat_item.lineclass = request.session['lineclassselected'],
            mat_item.diameter = request.session['diameterselected'],
            mat_item.quantity = request.POST['editPrefabQuantityBox'],
            mat_item.workpack = Workpack.objects.get(id=request.session['workpackselected']),
            mat_item.code = code,
            mat_item.datecreated = datetime.datetime.today(),
            mat_item.createdby = request.user.username

            mat_item.save()
            return HttpResponseRedirect('/prefabs/')

    return render_to_response('editprefab.html', context, context_instance=RequestContext(request))


def deleteprefabitem(request, materialitem_id):
    mat_item = MaterialItem.objects.get(id=materialitem_id)
    mat_item.delete()

    return HttpResponseRedirect('/prefabs/')


@login_required(login_url='/')
def showreinstateitems(request):
    context = dict()

    context['materialitems'] = MaterialItem.objects.filter(type__exact='Reinstatement')\
        .filter(workpack_id__exact=request.session['workpackselected'])

    context['workpacks'] = Workpack.objects.all()

    return render_to_response('reinstate.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def createreinstateitem(request):
    context = dict()

    if request.method == 'POST':

        if 'lineclassSelected' in request.POST:
            lclass = Lineclass.objects.filter(lineclassname=request.POST['lineclassSelected'])\
                .values_list('itemname', flat=True).distinct()
            request.session['lineclassselected'] = request.POST['lineclassSelected']
            lineclass = valuesquerysettodict(lclass)
            return HttpResponse(json.dumps(lineclass), content_type='application/json')

        if 'itemSelected' in request.POST:
            item = Lineclass.objects.filter(itemname=request.POST['itemSelected'])[0]
            diams = Lineclass.objects.filter(itemname=item.itemname).values_list('dn1', flat=True).distinct()
            request.session['itemselected'] = request.POST['itemSelected']
            diameters = valuesquerysettodict(diams)
            return HttpResponse(json.dumps(diameters), content_type='application/json')

        if 'diamSelected' in request.POST:
            request.session['diameterselected'] = request.POST['diamSelected']

        if 'addReinstateQuantityBox' in request.POST:
            code = Lineclass.objects.filter(lineclassname=request.session['lineclassselected'])\
                .filter(itemname=request.session['itemselected']).filter(dn1=request.session['diameterselected'])[0]\
                .code
            request.session['reinstatequantityselected'] = request.POST['addReinstateQuantityBox']
            mat_item = MaterialItem(
                name=request.session['itemselected'],
                type='Reinstatement',
                lineclass=request.session['lineclassselected'],
                diameter=request.session['diameterselected'],
                quantity=request.POST['addReinstateQuantityBox'],
                workpack=Workpack.objects.get(id=request.session['workpackselected']),
                code=code,
                datecreated=datetime.datetime.today(),
                createdby=request.user.username
            )

            mat_item.save()
            return HttpResponseRedirect('/reinstates/')

    return render_to_response('addreinstate.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def editreinstateitem(request, materialitem_id):
    context = dict()
    context['matitem'] = MaterialItem.objects.get(id=materialitem_id)

    if request.method == 'POST':

        if 'lineclassSelected' in request.POST:
            lclass = Lineclass.objects.filter(lineclassname=request.POST['lineclassSelected'])\
                .values_list('itemname', flat=True).distinct()
            request.session['lineclassselected'] = request.POST['lineclassSelected']
            lineclass = valuesquerysettodict(lclass)
            return HttpResponse(json.dumps(lineclass), content_type='application/json')

        if 'itemSelected' in request.POST:
            item = Lineclass.objects.filter(itemname=request.POST['itemSelected'])[0]
            diams = Lineclass.objects.filter(itemname=item.itemname).values_list('dn1', flat=True).distinct()
            request.session['itemselected'] = request.POST['itemSelected']
            diameters = valuesquerysettodict(diams)
            return HttpResponse(json.dumps(diameters), content_type='application/json')

        if 'diamSelected' in request.POST:
            request.session['diameterselected'] = request.POST['diamSelected']

        if 'editReinstateQuantityBox' in request.POST:
            code = Lineclass.objects.filter(lineclassname=request.session['lineclassselected'])\
                .filter(itemname=request.session['itemselected']).filter(dn1=request.session['diameterselected'])[0]\
                .code
            request.session['reinstatequantityselected'] = request.POST['editReinstateQuantityBox']
            mat_item = MaterialItem(
                name=request.session['itemselected'],
                type='Reinstatement',
                lineclass=request.session['lineclassselected'],
                diameter=request.session['diameterselected'],
                quantity=request.POST['editReinstateQuantityBox'],
                workpack=Workpack.objects.get(id=request.session['workpackselected']),
                code=code,
                datecreated=datetime.datetime.today(),
                createdby=request.user.username
            )
            return HttpResponseRedirect('/reinstates/')

    return render_to_response('reinstate.html', context, context_instance=RequestContext(request))


def deletereinstateitem(request, materialitem_id):
    mat_item = MaterialItem.objects.get(id=materialitem_id)
    mat_item.delete()
    return HttpResponseRedirect('/reinstates/')


@login_required(login_url='/')
def showspadingitems(request):
    context = dict()

    context['materialitems'] = MaterialItem.objects.filter(type__exact='Spading')\
        .filter(workpack_id__exact=request.session['workpackselected'])

    return render_to_response('spading.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def createspadingitem(request):
    context = dict()

    if request.method == 'POST':

        if 'lineclassSelected' in request.POST:
            lclass = Lineclass.objects.filter(lineclassname=request.POST['lineclassSelected'])\
                .values_list('itemname', flat=True).distinct()
            request.session['lineclassselected'] = request.POST['lineclassSelected']
            lineclass = valuesquerysettodict(lclass)
            return HttpResponse(json.dumps(lineclass), content_type='application/json')

        if 'itemSelected' in request.POST:
            item = Lineclass.objects.filter(itemname=request.POST['itemSelected'])[0]
            diams = Lineclass.objects.filter(itemname=item.itemname).values_list('dn1', flat=True).distinct()
            request.session['itemselected'] = request.POST['itemSelected']
            diameters = valuesquerysettodict(diams)
            return HttpResponse(json.dumps(diameters), content_type='application/json')

        if 'diamSelected' in request.POST:
            request.session['diameterselected'] = request.POST['diamSelected']

        if 'addSpadingQuantityBox' in request.POST:
            code = Lineclass.objects.filter(lineclassname=request.session['lineclassselected'])\
                .filter(itemname=request.session['itemselected']).filter(dn1=request.session['diameterselected'])[0]\
                .code
            request.session['spadingquantityselected'] = request.POST['addSpadingQuantityBox']
            mat_item = MaterialItem(
                name=request.session['itemselected'],
                type='Spading',
                lineclass=request.session['lineclassselected'],
                diameter=request.session['diameterselected'],
                quantity=request.POST['addSpadingQuantityBox'],
                workpack=Workpack.objects.get(id=request.session['workpackselected']),
                code=code,
                datecreated=datetime.datetime.today(),
                createdby=request.user.username
            )

            mat_item.save()
            return HttpResponseRedirect('/spadings/')

    return render_to_response('spading.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def editspadingitem(request, materialitem_id):
    context = dict()
    context['matitem'] = MaterialItem.objects.get(id=materialitem_id)

    if request.method == 'POST':

        if 'lineclassSelected' in request.POST:
            lclass = Lineclass.objects.filter(lineclassname=request.POST['lineclassSelected'])\
                .values_list('itemname', flat=True).distinct()
            request.session['lineclassselected'] = request.POST['lineclassSelected']
            lineclass = valuesquerysettodict(lclass)
            return HttpResponse(json.dumps(lineclass), content_type='application/json')

        if 'itemSelected' in request.POST:
            item = Lineclass.objects.filter(itemname=request.POST['itemSelected'])[0]
            diams = Lineclass.objects.filter(itemname=item.itemname).values_list('dn1', flat=True).distinct()
            request.session['itemselected'] = request.POST['itemSelected']
            diameters = valuesquerysettodict(diams)
            return HttpResponse(json.dumps(diameters), content_type='application/json')

        if 'diamSelected' in request.POST:
            request.session['diameterselected'] = request.POST['diamSelected']

        if 'editSpadingQuantityBox' in request.POST:
            code = Lineclass.objects.filter(lineclassname=request.session['lineclassselected'])\
                .filter(itemname=request.session['itemselected']).filter(dn1=request.session['diameterselected'])[0]\
                .code
            request.session['spadingquantityselected'] = request.POST['editSpadingQuantityBox']
            mat_item = MaterialItem(
                name=request.session['itemselected'],
                type='Spading',
                lineclass=request.session['lineclassselected'],
                diameter=request.session['diameterselected'],
                quantity=request.POST['editSpadingQuantityBox'],
                workpack=Workpack.objects.get(id=request.session['workpackselected']),
                code=code,
                datecreated=datetime.datetime.today(),
                createdby=request.user.username
            )
            return HttpResponseRedirect('/spadings/')

    return render_to_response('spading.html', context, context_instance=RequestContext(request))


def deletespadingitem(request, materialitem_id):
    mat_item = MaterialItem.objects.get(id=materialitem_id)
    mat_item.delete()
    return HttpResponseRedirect('/spadings/')