from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from .models import FieldWeldsBase, DemoLengthBase, InstallLengthBase, NumberOfHotCutsBase, \
    NumberOfColdCutsBase
from .models import SpadingNorms

from workpacks.models import Workpack

from .classes import FieldWeld, DemoLength, InstallLength, HotCut, ColdCut, EstimateTable

import datetime


def displayestimates(request):
    context = {}
    context.update(csrf(request))

    fieldweld_objects = FieldWeldsBase.objects.all()
    demolength_objects = DemoLengthBase.objects.all()
    installlength_objects = InstallLengthBase.objects.all()
    hotcut_objects = NumberOfHotCutsBase.objects.all()
    coldcut_objects = NumberOfColdCutsBase.objects.all()
    table = EstimateTable()

    context['masterlist'] = table.filter_values_into_table(fieldweld_objects, demolength_objects, installlength_objects,
                                                           hotcut_objects, coldcut_objects)
    print context['masterlist']

    context['demototals'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    context['installtotals'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    context['inspectiontotals'] = [0, 0]
    context['pressuretotals'] = [0, 0, 0, 0]

    return render_to_response('estimates.html', context, context_instance=RequestContext(request))


def getfieldweldbase(request):
    context = dict()
    context.update(csrf(request))
    if request.method == 'POST':
        if 'addFWLineclassBox' in request.POST:
            field_weld_item = FieldWeld(
                lineclass=request.POST['addFWLineclassBox'],
                diameter=request.POST['addFWDiameterBox'],
                quantity=request.POST['addFWQuantityBox']
            )
            saved_fw = FieldWeldsBase(
                lineclasses=field_weld_item.lineclass,
                diameter=field_weld_item.diameter,
                numberoffieldwelds=field_weld_item.quantity,
                created=datetime.datetime.today(),
                workpack=Workpack.objects.get(id=request.session['workpackselected'])
            )
            saved_fw.save()
            return HttpResponseRedirect('/estimates/')

    return render_to_response('addfieldweld.html', context, context_instance=RequestContext(request))


def getdemolengthbase(request):
    context = dict()
    context.update(csrf(request))
    if request.method == 'POST':
        if 'addDLLineclassBox' in request.POST:
            demo_length_item = DemoLength(
                lineclass=request.POST['addDLLineclassBox'],
                diameter=request.POST['addDLDiameterBox'],
                quantity=request.POST['addDLQuantityBox']
            )
            saved_dl = DemoLengthBase(
                lineclasses=demo_length_item.lineclass,
                diameter=demo_length_item.diameter,
                demolength=demo_length_item.quantity,
                created=datetime.datetime.today(),
                workpack=Workpack.objects.get(id=request.session['workpackselected'])
            )
            saved_dl.save()
            return HttpResponseRedirect('/estimates/')

    return render_to_response('adddemolength.html', context, context_instance=RequestContext(request))


def getinstalllengthbase(request):
    context = dict()
    context.update(csrf(request))
    if request.method == 'POST':
        if 'addILLineclassBox' in request.POST:
            install_length_item = InstallLength(
                lineclass=request.POST['addILLineclassBox'],
                diameter=request.POST['addILDiameterBox'],
                quantity=request.POST['addILQuantityBox']
            )
            saved_il = InstallLengthBase(
                lineclasses=install_length_item.lineclass,
                diameter=install_length_item.diameter,
                installlength=install_length_item.quantity,
                created=datetime.datetime.today(),
                workpack=Workpack.objects.get(id=request.session['workpackselected'])
            )
            saved_il.save()
            return HttpResponseRedirect('/estimates/')

    return render_to_response('addinstalllength.html', context, context_instance=RequestContext(request))


def getflangeptbase(request):
    fwcons = dict()

    if fwcons['flangepressuretestbaseform'].cleaned_data['flangehndlehotcut']:
        hotcutvar = 1 + SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform']
                                                    .cleaned_data['diameter_id'])[0].cuttingfactorhw - 1
    else:
        hotcutvar = 1

    if fwcons['flangepressuretestbaseform'].cleaned_data['alkybandc']:
        alkyvar = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform']
                                              .cleaned_data['diameter_id'])[0].alkyfactor_b_and_c_class - 1
    else:
        alkyvar = 0

    if fwcons['flangepressuretestbaseform'].cleaned_data['hacksawcutting']:
        hacksawvar = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform']
                                                 .cleaned_data['diameter_id'])[0].cuttingfactorhacksaw - 1
    else:
        hacksawvar = 0

    if fwcons['flangepressuretestbaseform'].cleaned_data['fambaset']:
        fambavar = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform']
                                               .cleaned_data['diameter_id'])[0].fambafactor - 1
    else:
        fambavar = 0

    numflanges = fwcons['flangepressuretestbaseform'].cleaned_data['numfpt']
    manhrs = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform']
                                         .cleaned_data['diameter_id'])[0].manhrs
    flangeptmanhours = {
        'installisoandpt': numflanges * manhrs * (hotcutvar + alkyvar + hacksawvar + fambavar)
    }

    if fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'] >= 10:
        riggersforiso = flangeptmanhours['installisoandpt']
    else:
        riggersforiso = 0

    return render_to_response('flangeptbase.html', fwcons, context_instance=RequestContext(request))


def getflangeribase(request):
    fwcons = dict()

    if fwcons['flangepressuretestbaseform'].cleaned_data['alkybandc']:
        alkyvar = 1 + SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform']
                                                  .cleaned_data['diameter_id'][0].alky_factor_b_and_c_class)-1
    else:
        alkyvar = 0

    if fwcons['flangepressuretestbaseform'].cleaned_data['fambaset']:
        fambavar = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform']
                                               .cleaned_data['diameter_id'][0].fambafactor)-1
    else:
        fambavar = 0

    rein1 = fwcons['flangereinstatebaseform'].cleaned_data['numfri']
    rein2 = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform']
                                        .cleaned_data['diameter_id'][0].manhrs)

    flamgerimanhours = {
        'reinstate': rein1 * rein2 * alkyvar + fambavar
    }

    if fwcons['flangereinstatebaseform'].cleaned_data['diameter_id'] >= 10:
        riggersforrein = flamgerimanhours['reinstate']
    else:
        riggersforrein = 0

    return render_to_response('flangeribase.html', fwcons, context_instance=RequestContext(request))


def calcnumberofjoints(formobj, pipenorm):

    boltupnorm = pipenorm.objects.filter(pipediameter__exact=formobj
                                         .cleaned_data['diameter_id'])[0].boltupjointnormhours
    numjoints = formobj.cleaned_data['numjoints']

    numjointsmanhours = {
        'unboltjointsfitter': numjoints * boltupnorm,
        'boltupjointsfitter': numjoints * boltupnorm
    }


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


def getnumberofcoldcuts(request):
    context = dict()
    context.update(csrf(request))
    if request.method == 'POST':
        if 'addCCLineclassBox' in request.POST:
            cold_cut_item = ColdCut(
                lineclass=request.POST['addCCLineclassBox'],
                diameter=request.POST['addCCDiameterBox'],
                quantity=request.POST['addCCQuantityBox']
            )
            if 'checkforcoldcutrig' in request.POST:
                riggercoldcut = True
            else:
                riggercoldcut = False
            saved_cc = NumberOfColdCutsBase(
                lineclasses=cold_cut_item.lineclass,
                diameter=cold_cut_item.diameter,
                numcoldcuts=cold_cut_item.quantity,
                created=datetime.datetime.today(),
                workpack=Workpack.objects.get(id=request.session['workpackselected']),
                rigforcoldcut=riggercoldcut
            )
            saved_cc.save()
            return HttpResponseRedirect('/estimates/')

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


def getnumberofhotcuts(request):
    context = dict()
    context.update(csrf(request))
    if request.method == 'POST':
        if 'addHCLineclassBox' in request.POST:
            hot_cut_item = HotCut(
                lineclass=request.POST['addHCLineclassBox'],
                diameter=request.POST['addHCDiameterBox'],
                quantity=request.POST['addHCQuantityBox']
            )
            if 'checkforhotcutrig' in request.POST:
                riggerhotcut = True
            else:
                riggerhotcut = False
            saved_hc = NumberOfHotCutsBase(
                lineclasses=hot_cut_item.lineclass,
                diameter=hot_cut_item.diameter,
                numhotcuts=hot_cut_item.quantity,
                created=datetime.datetime.today(),
                workpack=Workpack.objects.get(id=request.session['workpackselected']),
                rigforhotcut=riggerhotcut
            )
            saved_hc.save()
            return HttpResponseRedirect('/estimates/')

    return render_to_response('addhotcut.html', context, context_instance=RequestContext(request))