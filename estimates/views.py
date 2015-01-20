from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from .models import FieldWeldsBase, DemoLengthBase, InstallLengthBase, NumberOfHotCutsBase, \
    NumberOfColdCutsBase, Pipingnorms, FlangePressureTestBase, FlangeReinstateBase

from workpacks.models import Workpack

from .classes import FieldWeld, DemoLength, InstallLength, HotCut, ColdCut, EstimateTable

import datetime
import math


@login_required(login_url='/')
def displayestimates(request):
    context = {}
    context.update(csrf(request))

    fieldweld_objects = FieldWeldsBase.objects.all()
    demolength_objects = DemoLengthBase.objects.all()
    installlength_objects = InstallLengthBase.objects.all()
    hotcut_objects = NumberOfHotCutsBase.objects.all()
    coldcut_objects = NumberOfColdCutsBase.objects.all()

    table = EstimateTable()

    FieldWeld.totalgrindprep = 0
    FieldWeld.totalweldweld = 0
    FieldWeld.totalweldfit = 0
    FieldWeld.totalqcfitup = 0

    for fieldweld in fieldweld_objects:
        fieldweld = FieldWeld(fieldweld.lineclasses, fieldweld.diameter, fieldweld.numberoffieldwelds)
        fieldweld.calculate_manhours(Pipingnorms)

    context['fieldweldmanhours'] = {
        'totalGrindPrep': int(math.ceil(FieldWeld.totalgrindprep)),
        'totalWeldWeld': int(math.ceil(FieldWeld.totalweldweld)),
        'totalWeldFit': int(math.ceil(FieldWeld.totalweldfit)),
        'totalQcFitUp': int(math.ceil(FieldWeld.totalqcfitup))
    }

    DemoLength.total_rig_out_line_rigger = 0
    DemoLength.total_rig_out_line_fitter = 0
    DemoLength.total_rig_in_line_rigger = 0
    DemoLength.total_rig_in_line_fitter = 0

    for demolength in demolength_objects:
        demolength = DemoLength(demolength.lineclasses, demolength.diameter, demolength.demolength)
        demolength.calculate_manhours(Pipingnorms)

    context['demolengthmanhours'] = {
        'totalRigOutLineRigger': int(math.ceil(DemoLength.total_rig_out_line_rigger)),
        'totalRigOutLineFitter': int(math.ceil(DemoLength.total_rig_out_line_fitter)),
        'totalRigInLineRigger': int(math.ceil(DemoLength.total_rig_in_line_rigger)),
        'totalRigInLineFitter': int(math.ceil(DemoLength.total_rig_in_line_fitter))
    }

    InstallLength.total_rig_in_line_rigger = 0
    InstallLength.total_rig_in_line_fitter = 0

    for installlength in installlength_objects:
        installlength = InstallLength(installlength.lineclasses, installlength.diameter, installlength.installlength)
        installlength.calculate_manhours(Pipingnorms)

    context['installlengthmanhours'] = {
        'totalRigInLineRigger': int(math.ceil(InstallLength.total_rig_in_line_rigger)),
        'totalRigInLineFitter': int(math.ceil(InstallLength.total_rig_in_line_fitter))
    }

    context['bases'] = {
        'opsverifyspades':  1,
        'inspectionreportduration': 12,
        'inspectionreportresources': 1,
        'inspectionreportmanhours': 12,
        'prepareandpressureduration': 8,
        'carryoutflangemanageduration': 2,
        'carryoutflangemanageresources': 1,
        'carryoutflangemanagemanhours': 2,
        'saprefquality': 2,
        'saprefacceptance': 2
    }

    if request.method == 'POST':
        if 'erectScaffoldDuration' in request.POST:

            erectscaffoldmanhours = float(request.POST['erectScaffoldDuration']) / \
                float(request.POST['erectScaffoldScaffolders'])
            erectscaffoldmanhours = int(math.ceil(erectscaffoldmanhours))
            return HttpResponse(erectscaffoldmanhours)

        if 'removeInsulationDuration' in request.POST:

            removeinsulationmanhours = float(request.POST['erectScaffoldDuration']) / \
                float(request.POST['erectScaffoldScaffolders'])
            removeinsulationmanhours = int(math.ceil(removeinsulationmanhours))
            return HttpResponse(removeinsulationmanhours)

    context['masterlist'] = table.filter_values_into_table(fieldweld_objects, demolength_objects, installlength_objects,
                                                           hotcut_objects, coldcut_objects)

    return render_to_response('estimates.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def getfieldweldbase(request):
    context = dict()
    context.update(csrf(request))
    fieldwelds = FieldWeldsBase.objects.all()
    if request.method == 'POST':
        if 'lcSelected' in request.POST:
            for fieldweld in fieldwelds:
                if request.POST['lcSelected'] in fieldweld.lineclasses:
                    request.session['lineclassexists'] = True

            request.session['lcSelected'] = request.POST['lcSelected']
            if request.session['lineclassexists']:
                exists = 'True'
                return HttpResponse(exists)

        if 'answer' in request.POST:
            fw = FieldWeldsBase.objects.filter(lineclasses=request.session['lcSelected'])\
                .filter(workpack=request.session['workpackselected'])[0]
            if request.POST['answer'] == 'True':
                fw.numberoffieldwelds += float(request.POST['quantity'])
                fw.diameter = request.POST['diameter']
                fw.save()

            if request.POST['answer'] == 'False':
                fw.delete()
                fw_item = FieldWeldsBase(
                    lineclasses=request.session['lcSelected'],
                    diameter=request.POST['diameter'],
                    numberoffieldwelds=request.POST['quantity'],
                    created=datetime.datetime.today(),
                    workpack=Workpack.objects.get(id=request.session['workpackselected'])
                )
                fw_item.save()

    return render_to_response('addfieldweld.html', context, context_instance=RequestContext(request))


def deletefieldweldbase(request, fieldweld_id):
    fw_item = FieldWeldsBase.objects.get(id=fieldweld_id)
    fw_item.delete()
    return HttpResponseRedirect('/estimates/')


@login_required(login_url='/')
def getdemolengthbase(request):
    context = dict()
    context.update(csrf(request))

    demolengths = DemoLengthBase.objects.all()
    if request.method == 'POST':
        if 'lcSelected' in request.POST:
            for demolength in demolengths:
                if request.POST['lcSelected'] in demolength.lineclasses:
                    request.session['lineclassexists'] = True

            request.session['lcSelected'] = request.POST['lcSelected']
            if request.session['lineclassexists']:
                exists = 'True'
                return HttpResponse(exists)

        if 'answer' in request.POST:
            dl = DemoLengthBase.objects.filter(lineclasses=request.session['lcSelected'])\
                .filter(workpack=request.session['workpackselected'])[0]
            if request.POST['answer'] == 'True':
                dl.demolength += float(request.POST['quantity'])
                dl.diameter = request.POST['diameter']
                dl.save()

            if request.POST['answer'] == 'False':
                dl.delete()
                dl_item = DemoLengthBase(
                    lineclasses=request.session['lcSelected'],
                    diameter=request.POST['diameter'],
                    demolength=request.POST['quantity'],
                    created=datetime.datetime.today(),
                    workpack=Workpack.objects.get(id=request.session['workpackselected'])
                )
                dl_item.save()

    return render_to_response('adddemolength.html', context, context_instance=RequestContext(request))


def deletedemolengthbase(request, demolength_id):
    dl_item = DemoLengthBase.objects.get(id=demolength_id)
    dl_item.delete()
    return HttpResponseRedirect('/estimates/')


@login_required(login_url='/')
def getinstalllengthbase(request):
    context = dict()
    context.update(csrf(request))

    installlengths = InstallLengthBase.objects.all()
    if request.method == 'POST':
        if 'lcSelected' in request.POST:
            for installlength in installlengths:
                if request.POST['lcSelected'] in installlength.lineclasses:
                    request.session['lineclassexists'] = True

            request.session['lcSelected'] = request.POST['lcSelected']
            if request.session['lineclassexists']:
                exists = 'True'
                return HttpResponse(exists)

        if 'answer' in request.POST:
            il = InstallLengthBase.objects.filter(lineclasses=request.session['lcSelected'])\
                .filter(workpack=request.session['workpackselected'])[0]
            if request.POST['answer'] == 'True':
                il.installlength += float(request.POST['quantity'])
                il.diameter = request.POST['diameter']
                il.save()

            if request.POST['answer'] == 'False':
                il.delete()
                il_item = InstallLengthBase(
                    lineclasses=request.session['lcSelected'],
                    diameter=request.POST['diameter'],
                    installlength=request.POST['quantity'],
                    created=datetime.datetime.today(),
                    workpack=Workpack.objects.get(id=request.session['workpackselected'])
                )
                il_item.save()

    return render_to_response('addinstalllength.html', context, context_instance=RequestContext(request))


def deleteinstalllengthbase(request, demolength_id):
    il_item = InstallLengthBase.objects.get(id=demolength_id)
    il_item.delete()
    return HttpResponseRedirect('/estimates/')


@login_required(login_url='/')
def getflangeptbase(request):
    context = dict()
    context.update(csrf(request))

    if request.method == 'POST':
        if 'addFlangeLineclassCombo' in request.POST:
            if 'addFlangeHacksaw' in request.POST:
                hacksaw = True
            else:
                hacksaw = False
            if 'addFlangeHotCut' in request.POST:
                hotcut = True
            else:
                hotcut = False
            if 'addFlangeAlky' in request.POST:
                alky = True
            else:
                alky = False
            if 'addFlangeBASet' in request.POST:
                baset = True
            else:
                baset = False
            flange_pt = FlangePressureTestBase(
                lineclasses=request.POST['addFlangeLineclassCombo'],
                diameter=request.POST['addFlangeDiameterCombo'],
                numfpt=request.POST['addFlangeQuantityBox'],
                created=datetime.datetime.today(),
                workpack=Workpack.objects.get(id=request.session['workpackselected']),
                flangehndlehotcut=hotcut,
                alkybandc=alky,
                hacksawcutting=hacksaw,
                fambaset=baset
            )

            flange_pt.save()
            return HttpResponseRedirect('/estimates/')

    return render_to_response('addflangept.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def getflangeribase(request):
    context = dict()
    context.update(csrf(request))

    if request.method == 'POST':
        if 'addFlangeLineclassCombo' in request.POST:
            if 'addFlangeAlky' in request.POST:
                alky = True
            else:
                alky = False
            if 'addFlangeBASet' in request.POST:
                baset = True
            else:
                baset = False
            flange_ri = FlangeReinstateBase(
                lineclasses=request.POST['addFlangeLineclassCombo'],
                diameter=request.POST['addFlangeDiameterCombo'],
                numfri=request.POST['addFlangeQuantityBox'],
                created=datetime.datetime.today(),
                workpack=Workpack.objects.get(id=request.session['workpackselected']),
                alkybandc=alky,
                fambaset=baset
            )

            flange_ri.save()
            return HttpResponseRedirect('/estimates/')

    return render_to_response('addflangeri.html', context, context_instance=RequestContext(request))


def calcnumberofjoints(formobj, pipenorm):

    boltupnorm = pipenorm.objects.filter(pipediameter__exact=formobj
                                         .cleaned_data['diameter_id'])[0].boltupjointnormhours
    numjoints = formobj.cleaned_data['numjoints']

    numjointsmanhours = {
        'unboltjointsfitter': numjoints * boltupnorm,
        'boltupjointsfitter': numjoints * boltupnorm
    }


@login_required(login_url='/')
def getnumberofjoints(request):
    fwcons = dict()

    return render_to_response('numjointsbase.html', fwcons, context_instance=RequestContext(request))


def calcnumberofcoldcuts(formobj, pipenorm):

    coldcutnorm = pipenorm.objects.filter(pipediameter__exact=formobj.cleaned_data['diameter_id'])[0].coldcutnormhours
    numcuts = formobj.cleaned_data['numcoldcuts']

    coldcutmanhours = {
        'coldcutline': coldcutnorm * numcuts * 1
    }

    if formobj.cleaned_data['diameter_id'] >= 4:
        riggersforcoldcut = coldcutmanhours['coldcutline']
    else:
        riggersforcoldcut = 0


@login_required(login_url='/')
def getnumberofcoldcuts(request):
    context = dict()
    context.update(csrf(request))

    coldcuts = NumberOfColdCutsBase.objects.all()
    if request.method == 'POST':
        if 'lcSelected' in request.POST:
            for coldcut in coldcuts:
                if request.POST['lcSelected'] in coldcut.lineclasses:
                    request.session['lineclassexists'] = True

            request.session['lcSelected'] = request.POST['lcSelected']
            if request.session['lineclassexists']:
                exists = 'True'
                return HttpResponse(exists)

        if 'answer' in request.POST:
            cc = NumberOfColdCutsBase.objects.filter(lineclasses=request.session['lcSelected'])\
                .filter(workpack=request.session['workpackselected'])[0]
            if request.POST['answer'] == 'True':
                cc.numcoldcuts += float(request.POST['quantity'])
                cc.diameter = request.POST['diameter']
                cc.save()

            if request.POST['answer'] == 'False':
                cc.delete()
                cc_item = NumberOfColdCutsBase(
                    lineclasses=request.session['lcSelected'],
                    diameter=request.POST['diameter'],
                    numcoldcuts=request.POST['quantity'],
                    created=datetime.datetime.today(),
                    workpack=Workpack.objects.get(id=request.session['workpackselected'])
                )
                cc_item.save()

    return render_to_response('addcoldcut.html', context, context_instance=RequestContext(request))


def calcnumberofhotcuts(formobj, pipenorm):

    hotcutnorm = pipenorm.objects.filter(pipediameter__exact=formobj.cleaned_data['diameter_id'])[0].hotcutnormhours
    numcuts = formobj.cleaned_data['numhotcuts']

    hotcutmanhours = {
        'hotcutline': hotcutnorm * numcuts * 1
    }

    if formobj.cleaned_data['diameter_id'] >= 4:
        riggersforhotcut = hotcutmanhours['hotcutline']
    else:
        riggersforhotcut = 0

    return hotcutmanhours


@login_required(login_url='/')
def getnumberofhotcuts(request):
    context = dict()
    context.update(csrf(request))

    hotcuts = NumberOfHotCutsBase.objects.all()
    if request.method == 'POST':
        if 'lcSelected' in request.POST:
            for hotcut in hotcuts:
                if request.POST['lcSelected'] in hotcut.lineclasses:
                    request.session['lineclassexists'] = True

            request.session['lcSelected'] = request.POST['lcSelected']
            if request.session['lineclassexists']:
                exists = 'True'
                return HttpResponse(exists)

        if 'answer' in request.POST:
            hc = NumberOfHotCutsBase.objects.filter(lineclasses=request.session['lcSelected'])\
                .filter(workpack=request.session['workpackselected'])[0]
            if request.POST['answer'] == 'True':
                hc.numhotcuts += float(request.POST['quantity'])
                hc.diameter = request.POST['diameter']
                hc.save()

            if request.POST['answer'] == 'False':
                hc.delete()
                hc_item = InstallLengthBase(
                    lineclasses=request.session['lcSelected'],
                    diameter=request.POST['diameter'],
                    numhotcuts=request.POST['quantity'],
                    created=datetime.datetime.today(),
                    workpack=Workpack.objects.get(id=request.session['workpackselected'])
                )
                hc_item.save()

    return render_to_response('addhotcut.html', context, context_instance=RequestContext(request))