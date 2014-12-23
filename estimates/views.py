from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from .models import Pipingnorms, FieldWeldsBase
from .models import SpadingNorms

from workpacks.models import Workpack

import math

from .forms import FieldWeldsBaseForm, DemoLengthBaseForm, InstallLengthBaseForm, FlangePressureTestBaseForm
from .forms import FlangeReinstateBaseForm, NumberOfJointsBaseForm, NumberOfColdCutsBaseForm, NumberOfHotCutsBaseForm


def createestimates(request):
    createestcons = {}
    createestcons.update(csrf(request))
    try:
        createestcons['workpacks'] = Workpack.objects.all()
    except KeyError:
        Workpack.DoesNotExist()

    fieldwelds = FieldWeldsBase.objects.all()

    # Store each of the saves into a list...
    fieldweldvalues = []
    for fieldweld in fieldwelds:
        fieldweldvalues.append(calcfieldwelds(fieldweld, Pipingnorms))

    # Temporary vars to hold values extracted from each tuple(fieldweld)...
    totalqc = 0
    totalgp = 0
    totalww = 0
    totalwf = 0

    for value in fieldweldvalues:
        totalqc += value[0]
        totalgp += value[1]
        totalww += value[2]
        totalwf += value[3]

    createestcons['fieldweldbase'] = {
        'qcfitupcheck': int(math.ceil(totalqc)),
        'grindprep': int(math.ceil(totalgp)),
        'weldweld': int(math.ceil(totalww)),
        'weldfit': int(math.ceil(totalwf))
    }

    createestcons['opsverify'] = {
        'duration': 1,
    }

    createestcons['installisoandpt'] = {
        'duration': 0,
    }

    createestcons['opspermit'] = {
        'resources': 1,
        'duration': 4,
        'manhours': 4
    }

    createestcons['inspectionreport'] = {
        'inspection': 1,
        'manhours': 12,
        'duration': 12
    }

    createestcons['prepareandpressure'] = {
        'resources': 0,
        'manhours': 0,
        'duration': 8
    }

    createestcons['flangemanage'] = {
        'resources': 1,
        'manhours': 2,
        'duration': 2
    }

    createestcons['saprefquality'] = {
        'duration': 2
    }

    createestcons['saprefaccept'] = {
        'duration': 2
    }

    createestcons['powerbrush'] = {
        'duration': 0
    }

    createestcons['unboltjoints'] = {
        'duration': 0
    }

    createestcons['riggingactivitiesrigout'] = {
        'duration': 0
    }

    createestcons['coldcutline'] = {
        'duration': 0
    }

    createestcons['hotcutline'] = {
        'duration': 0
    }

    createestcons['dismantlesteam'] = {
        'duration': 0
    }

    createestcons['hpflushing'] = {
        'duration': 0
    }

    createestcons['executiontotal'] = {
        'insulationduration': 0,
        'mfitterduration': createestcons['installisoandpt']['duration'] + createestcons['powerbrush']['duration'] +
        createestcons['unboltjoints']['duration'],
        'riggersduration': createestcons['riggingactivitiesrigout']['duration'],
        'scafoldersduration': 0,
        'pfitterduration': createestcons['opspermit']['duration'] + createestcons['coldcutline']['duration'] +
        createestcons['hotcutline']['duration'] + createestcons['dismantlesteam']['duration'] +
        createestcons['riggingactivitiesrigout']['duration'],
        'hydrojettingduration': createestcons['hpflushing']['duration']
    }

    return render_to_response('page2.html', createestcons, context_instance=RequestContext(request))


def calcfieldwelds(fieldwelditem, pipnorm):
    cutnorm = pipnorm.objects.filter(pipediameter__exact=fieldwelditem.diameter)[0].cut
    prepnorm = pipnorm.objects.filter(pipediameter__exact=fieldwelditem.diameter)[0].prep
    numberfieldwelds = fieldwelditem.numberoffieldwelds
    weldernorm = pipnorm.objects.filter(pipediameter__exact=fieldwelditem.diameter)[0].tackweldlesseighty
    fieldweldhours = {
        'grindprep': (cutnorm + prepnorm) * 2 * weldernorm * 1,
        'weldweld': weldernorm * numberfieldwelds * 1,
        'qcfitupcheck': 1 * numberfieldwelds
    }

    print 'Grind Prep %f' % fieldweldhours['grindprep']
    print 'Weld Weld %f' % fieldweldhours['weldweld']

    print 'WC Fitup %f' % fieldweldhours['qcfitupcheck']

    if fieldwelditem.diameter < 4:
        fieldweldhours['weldfit'] = fieldweldhours['weldweld'] * 0.15
    else:
        fieldweldhours['weldfit'] = fieldweldhours['weldweld'] * 0.30

    print 'Weld Fit %f' % fieldweldhours['weldfit']

    return fieldweldhours['qcfitupcheck'], fieldweldhours['grindprep'], fieldweldhours['weldweld'], fieldweldhours['weldfit']


def getfieldweldbase(request):
    fwcons = dict()

    fwcons['fieldweldsbaseform'] = FieldWeldsBaseForm(request.POST or None)
    if fwcons['fieldweldsbaseform'].is_valid():
        savedform = fwcons['fieldweldsbaseform'].save(commit=False)
        savedform.workpack = Workpack.objects.get(id=request.session['workpackselected'])
        savedform.save()

        return HttpResponseRedirect('/new-estimates/')
    else:
        print fwcons['fieldweldsbaseform'].errors

    return render_to_response('newfieldweld.html', fwcons, context_instance=RequestContext(request))


def calcdemolength(formobj, pipenorms):
    rig1 = pipenorms.objects.filter(pipediameter__exact=formobj.cleaned_data['diameter_id'])[0].handlemeternormshours
    rig2 = formobj.cleaned_data['demolength']
    demolengthhours = {
        'rigoutlinerig': rig1 * rig2
    }

    demolengthhours['rigoutlinefit'] = demolengthhours['rigoutlinerig']

    demolengthhours['rigoutlinefit'] = demolengthhours['rigoutlinerig']
    demolengthhours['riginlinerigdemo'] = demolengthhours['rigoutlinerig']
    demolengthhours['riginlinefitdemo'] = demolengthhours['rigoutlinerig']
    return demolengthhours


def getdemolengthbase(request):
    fwcons = dict()
    fwcons['demolengthbaseform'] = DemoLengthBaseForm(request.POST or None)
    if fwcons['demolengthbaseform'].is_valid():
        fwcons['demolengthbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['demolengthbaseform'].save()

        calcdemolength(fwcons['demolengthbaseform'], Pipingnorms)

        return HttpResponseRedirect('/')
    else:
        print fwcons['demolengthbaseform'].errors

    return render_to_response('demolengthbase.html', fwcons, context_instance=RequestContext(request))


def calcinstalllength(formobj, pipnorms):
    rig1 = pipnorms.objects.filter(pipediameter__exact=formobj.cleaned_data['diameter_id'])[0].handlemeternormshours
    rig2 = formobj.cleaned_data['installlength']
    installlengthmanhours = {
        'riginlinerig': rig1 * rig2
    }

    installlengthmanhours['riginlinefit'] = installlengthmanhours['riginlinerig']

    return installlengthmanhours


def getinstalllengthbase(request):

    fwcons = dict()
    fwcons['installlengthbaseform'] = InstallLengthBaseForm(request.POST or None)
    if fwcons['installlengthbaseform'].is_valid():
        fwcons['installlengthbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['installlengthbaseform'].save()

        calcinstalllength(fwcons['installlengthbaseform'], Pipingnorms)

        return HttpResponseRedirect('/')
    else:
        print fwcons['installlengthbaseform'].errors

    return render_to_response('newinstalllength.html', fwcons, context_instance=RequestContext(request))


def getflangeptbase(request):
    fwcons = dict()
    fwcons['flangepressuretestbaseform'] = FlangePressureTestBaseForm(request.POST or None)
    if fwcons['flangepressuretestbaseform'].is_valid():
        fwcons['flangepressuretestbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['flangepressuretestbaseform'].save()

        if fwcons['flangepressuretestbaseform'].cleaned_data['flangehndlehotcut']:
            hotcutvar = 1 + SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'])[0].cuttingfactorhw - 1
        else:
            hotcutvar = 1

        if fwcons['flangepressuretestbaseform'].cleaned_data['alkybandc']:
            alkyvar = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'])[0].alkyfactor_b_and_c_class - 1
        else:
            alkyvar = 0

        if fwcons['flangepressuretestbaseform'].cleaned_data['hacksawcutting']:
            hacksawvar = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'])[0].cuttingfactorhacksaw - 1
        else:
            hacksawvar = 0

        if fwcons['flangepressuretestbaseform'].cleaned_data['fambaset']:
            fambavar = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'])[0].fambafactor - 1
        else:
            fambavar = 0

        numflanges = fwcons['flangepressuretestbaseform'].cleaned_data['numfpt']
        manhrs = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'])[0].manhrs
        flangeptmanhours = {
            'installisoandpt': numflanges * manhrs * (hotcutvar + alkyvar + hacksawvar + fambavar)
        }

        if fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'] >= 10:
            riggersforiso = flangeptmanhours['installisoandpt']
        else:
            riggersforiso = 0

        return HttpResponseRedirect('/')
    else:
        print fwcons['flangepressuretestbaseform'].errors

    return render_to_response('flangeptbase.html', fwcons, context_instance=RequestContext(request))


def getflangeribase(request):
    fwcons = dict()
    fwcons['flangereinstatebaseform'] = FlangeReinstateBaseForm(request.POST or None)
    if fwcons['flangereinstatebaseform'].is_valid():
        fwcons['flangereinstatebaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['flangereinstatebaseform'].save()

        if fwcons['flangepressuretestbaseform'].cleaned_data['alkybandc']:
            alkyvar = 1 + SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'][0].alky_factor_b_and_c_class)-1
        else:
            alkyvar = 0

        if fwcons['flangepressuretestbaseform'].cleaned_data['fambaset']:
            fambavar = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'][0].fambafactor)-1
        else:
            fambavar = 0

        rein1 = fwcons['flangereinstatebaseform'].cleaned_data['numfri']
        rein2 = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'][0].manhrs)

        flamgerimanhours = {
            'reinstate': rein1 * rein2 * alkyvar + fambavar
        }

        if fwcons['flangereinstatebaseform'].cleaned_data['diameter_id'] >= 10:
            riggersforrein = flamgerimanhours['reinstate']
        else:
            riggersforrein = 0

        return HttpResponseRedirect('/')
    else:
        print fwcons['flangereinstatebaseform'].errors

    return render_to_response('flangeribase.html', fwcons, context_instance=RequestContext(request))


def calcnumberofjoints(formobj, pipenorm):

    boltupnorm = pipenorm.objects.filter(pipediameter__exact=formobj.cleaned_data['diameter_id'])[0].boltupjointnormhours
    numjoints = formobj.cleaned_data['numjoints']

    numjointsmanhours = {
        'unboltjointsfitter': numjoints * boltupnorm,
        'boltupjointsfitter': numjoints * boltupnorm
    }


    if formobj.cleaned_data['instrumentsboltup']:
        instrumentsBool.append(True)
    else:
        instrumentsBool.append(False)

    for boolval in instrumentsBool:
        if boolval:
            disconnectinstruments = 3
        else:
            disconnectinstruments = 0

    if formobj.cleaned_data['rigforjoints']:
        riggersforunbolt = numjointsmanhours['unboltjointsfitter']
        riggersforboltup = numjointsmanhours['boltupjointsfitter']

    return numjointsmanhours


def getnumberofjoints(request):
    fwcons = dict()

    fwcons['numberofjointsbaseform'] = NumberOfJointsBaseForm(request.POST or None)
    if fwcons['numberofjointsbaseform'].is_valid():
        fwcons['numberofjointsbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['numberofjointsbaseform'].save()

        calcnumberofjoints(fwcons['numberofjointsbaseform'], Pipingnorms)

        return HttpResponseRedirect('/')
    else:
        print fwcons['numberofjointsbaseform'].errors

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
    fwcons = dict()
    fwcons['numberofcoldcutsbaseform'] = NumberOfColdCutsBaseForm(request.POST or None)
    if fwcons['numberofcoldcutsbaseform'].is_valid():
        fwcons['numberofcoldcutsbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['numberofcoldcutsbaseform'].save()

        calcnumberofcoldcuts(fwcons['numberofcoldcutsbaseform'], Pipingnorms)

        return HttpResponseRedirect('/')
    else:
        print fwcons['numberofcoldcutsbaseform'].errors

    return render_to_response('numcoldcutsbase.html', fwcons, context_instance=RequestContext(request))


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
    fwcons = dict()

    fwcons['numberofhotcutsbaseform'] = NumberOfHotCutsBaseForm(request.POST or None)
    if fwcons['numberofhotcutsbaseform'].is_valid():
        fwcons['numberofhotcutsbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['numberofhotcutsbaseform'].save()

        calcnumberofhotcuts(fwcons['numberofhotcutsbaseform'], Pipingnorms)

        return HttpResponseRedirect('/')
    else:
        print fwcons['numberofhotcutsbaseform'].errors

    return render_to_response('numhotcutsbase.html', fwcons, context_instance=RequestContext(request))


def editfieldweld(request, fieldweld_id):
    editfwcons = dict()
    editfwcons['fieldweld'] = FieldWeldsBase.objects.get(fieldweld_id=fieldweld_id)
    return render_to_response('editfieldwelds.html', editfwcons, context_instance=RequestContext(request))


def deletefieldweld(request, fieldweld_id):
    editfwcons = dict()
    editfwcons['fieldweld'] = FieldWeldsBase.objects.get(fieldweld_id=fieldweld_id)
    editfwcons['fieldweld'].delete()
    return HttpResponseRedirect('/new-estimates/')