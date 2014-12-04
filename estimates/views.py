from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from .models import EstimateDefaults, Pipingnorms, Manhoursfactor, FieldWeldsBase, FieldWeldsHours
from .models import DemoLengthBase

from workpacks.models import Workpack, Lineclasses
from materials.models import SizeList

from fractions import Fraction
import math

from .forms import FieldWeldHoursForm, FieldWeldsBaseForm, DemoLengthBaseForm, InstallLengthBaseForm, FlangePressureTestBaseForm
from .forms import FlangeReinstateBaseForm, NumberOfJointsBaseForm, NumberOfColdCutsBaseForm, NumberOfHotCutsBaseForm


def createestimates(request):
    createestcons = {}
    createestcons.update(csrf(request))
    createestcons['workpacks'] = Workpack.objects.all()

    createestcons['opsverify'] = {
        'duration': 1,
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

    createestcons['total'] = {
        'duration': createestcons['inspectionreport']['duration'] + createestcons['prepareandpressure']['duration']
        + createestcons['flangemanage']['duration'] + createestcons['saprefquality']['duration'] +
        createestcons['saprefaccept']['duration'] + createestcons['opsverify']['duration'],
        'manhours':  createestcons['inspectionreport']['manhours'] + createestcons['prepareandpressure']['manhours']
        + createestcons['flangemanage']['manhours']
    }

    createestcons['fieldweldbase'] = FieldWeldsBase.objects.all()
    createestcons['fieldweldhours'] = FieldWeldsHours.objects.all()

    return render_to_response('newestimate.html', createestcons, context_instance=RequestContext(request))


def calculateresources(request):
    caclrescons = dict()

    # Get the base estimates given by the user...
    basestimate = EstimateDefaults.objects.get(workpack_id=request.session['workpackselected'])

    # The material factor...
    pmfac = Manhoursfactor.objects.filter(material__exact=basestimate.material)[0].pfitter
    # wmfac = Manhoursfactor.objects.filter(material__exact=basestimate.material)[0].wfitter

    tackandweldweldernorm = basestimate.schedule

    hotcutnorm = Pipingnorms.objects.filter(pipediameter__exact=basestimate.diameter)[0].hotcutnormhours
    boltupnormfitter = Pipingnorms.objects.filter(pipediameter__exact=basestimate.diameter)[0].boltupjointnormhours
    riglinenorm = Pipingnorms.objects.filter(pipediameter__exact=basestimate.diameter)[0].handlemeternormshours
    cutnorm = Pipingnorms.objects.filter(pipediameter__exact=basestimate.diameter)[0].cut
    prepnorm = Pipingnorms.objects.filter(pipediameter__exact=basestimate.diameter)[0].prep

    if tackandweldweldernorm == 80:
        schedulenorm = Pipingnorms.objects.filter(pipediameter__exact=basestimate.diameter)[0].tackweldgreateighty
    else:
        schedulenorm = Pipingnorms.objects.filter(pipediameter__exact=basestimate.diameter)[0].tackweldlesseighty

    result = {
        'coldcutmanhours': basestimate.numberofcoldcuts * coldcutnorm * pmfac,

        'hotcutmanhours': basestimate.numberofhotcuts * hotcutnorm * pmfac,

        'tackandweldwelderhours': basestimate.fieldwelds * schedulenorm * pmfac,

        'boltupjointshoursfitter': basestimate.numberofjoints * boltupnormfitter,

        'rigoutlinehours': basestimate.demolength * riglinenorm,

        'riginlinehours': basestimate.installlength * riglinenorm,

        'grindprepfithours': basestimate.fieldwelds * (cutnorm + prepnorm) * 2
    }

    result['unboltjointshoursfitter'] = result['boltupjointshoursfitter']

    fracestimate = Fraction(basestimate.diameter)

    if basestimate.riggersforboltup:
        boltupjointhoursriggers = result['boltupjointshoursfitter']
        unboltjointhoursriggers = result['unboltjointshoursfitter']
    else:
        boltupjointhoursriggers = 0
        unboltjointhoursriggers = 0

    result['boltupjointshoursrigger'] = boltupjointhoursriggers
    result['unboltjointshoursrigger'] = unboltjointhoursriggers

    if fracestimate > 4:
        tackandweldfitterhours = result['tackandweldwelderhours'] * 0.3
    else:
        tackandweldfitterhours = result['tackandweldwelderhours'] * 0.15

    result['tackandweldfitterhours'] = tackandweldfitterhours

    if fracestimate < 4:
        riggersforcoldcut = 0
        riggersforhotcut = 0
    else:
        riggersforcoldcut = result['coldcutmanhours']
        riggersforhotcut = result['hotcutmanhours']

    result['riggersforcoldcut'] = riggersforcoldcut
    result['riggersforhotcut'] = riggersforhotcut

    print result

    return render_to_response('getresources.html', caclrescons, context_instance=RequestContext(request))


def getfieldweldhours(request):
    fwcons = dict()
    fwcons['fieldweldshoursform'] = FieldWeldHoursForm(request.POST or None)
    if fwcons['fieldweldshoursform'].is_valid():
        fwcons['fieldweldshoursform'].save()
        return HttpResponseRedirect('/')
    else:
        print fwcons['fieldweldshoursform'].errors

    return render_to_response('fieldweldhours.html', fwcons, context_instance=RequestContext(request))


def getfieldweldbase(request):
    fwcons = dict()
    schedule80 = [0.5, 0.75, 1, 1.5]
    schedule40 = [2, 3, 4, 6]
    schedule20 = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

    fwcons['fieldweldsbaseform'] = FieldWeldsBaseForm(request.POST or None)
    if fwcons['fieldweldsbaseform'].is_valid():
        fwcons['fieldweldsbaseform'].save()
        fwcons['fieldweldsbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        if fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'] in schedule40:
            grind1 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'])[0].prep
            grind2 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'])[0].tackweldlesseighty
            grind3 = fwcons['fieldweldsbaseform'].cleaned_data['numberoffieldwelds']
            weld1 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'])[0].tackweldlesseighty
            fieldweldsduration = {
                'grindprep': grind1 + grind2 * 2 * grind3 * 1,
                'weldweld': weld1 * grind3 * 1
            }
            if fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'] > 4:
                fieldweldsduration['weldfit'] = math.ceil(fieldweldsduration['weldweld'] * 0.15)
            else:
                fieldweldsduration['weldfit'] = math.ceil(fieldweldsduration['weldweld'] * 0.3)

        return HttpResponseRedirect('/new-estimates/')
    else:
        print fwcons['fieldweldsbaseform'].errors

    return render_to_response('newfieldweld.html', fwcons, context_instance=RequestContext(request))


def getdemolengthbase(request):
    fwcons = dict()
    fwcons['demolengthbaseform'] = DemoLengthBaseForm(request.POST or None)
    if fwcons['demolengthbaseform'].is_valid():
        fwcons['demolengthbaseform'].save()
        rig1 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['demolengthbaseform'].cleaned_data['diameter_id'])[0].handlemeternormshours
        rig2 = fwcons['demolengthbaseform'].cleaned_data['demolength']
        demolengthmanhours = {
            'rigoutlinerig': rig1 * rig2
        }

        demolengthmanhours['rigoutlinefit'] = demolengthmanhours['rigoutlinerig']

        return HttpResponseRedirect('/')
    else:
        print fwcons['demolengthbaseform'].errors

    return render_to_response('demolengthbase.html', fwcons, context_instance=RequestContext(request))


def getinstalllengthbase(request):
    fwcons = dict()
    fwcons['installlengthbaseform'] = InstallLengthBaseForm(request.POST or None)
    if fwcons['installlengthbaseform'].is_valid():
        fwcons['installlengthbaseform'].save()
        rig1 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['installlengthbaseform'].cleaned_data['diameter_id'])[0].handlemeternormshours
        rig2 = fwcons['installlengthbaseform'].cleaned_data['installlength']
        demolengthmanhours = {
            'rigoutlinerig': rig1 * rig2
        }

        demolengthmanhours['rigoutlinefit'] = demolengthmanhours['rigoutlinerig']

        return HttpResponseRedirect('/')
    else:
        print fwcons['installlengthbaseform'].errors

    return render_to_response('installlengthbase.html', fwcons, context_instance=RequestContext(request))


def getflangeptbase(request):
    fwcons = dict()
    fwcons['flangepressuretestbaseform'] = FlangePressureTestBaseForm(request.POST or None)
    if fwcons['flangepressuretestbaseform'].is_valid():
        fwcons['flangepressuretestbaseform'].save()
        instiso1 = ''
        flamgeptmanhours = {
            'installisolation': ''
        }

        return HttpResponseRedirect('/')
    else:
        print fwcons['flangepressuretestbaseform'].errors

    return render_to_response('flangeptbase.html', fwcons, context_instance=RequestContext(request))


def getflangeribase(request):
    fwcons = dict()
    fwcons['flangereinstatebaseform'] = FlangeReinstateBaseForm(request.POST or None)
    if fwcons['flangereinstatebaseform'].is_valid():
        fwcons['flangereinstatebaseform'].save()
        flamgerimanhours = {

        }

        return HttpResponseRedirect('/')
    else:
        print fwcons['flangereinstatebaseform'].errors

    return render_to_response('flangeribase.html', fwcons, context_instance=RequestContext(request))


def getnumberofjoints(request):
    fwcons = dict()
    fwcons['numberofjointsbaseform'] = NumberOfJointsBaseForm(request.POST or None)
    if fwcons['numberofjointsbaseform'].is_valid():
        fwcons['numberofjointsbaseform'].save()
        flamgerimanhours = {

        }

        return HttpResponseRedirect('/')
    else:
        print fwcons['numberofjointsbaseform'].errors

    return render_to_response('numjointsbase.html', fwcons, context_instance=RequestContext(request))


def getnumberofcoldcuts(request):
    fwcons = dict()
    fwcons['numberofcoldcutsbaseform'] = NumberOfColdCutsBaseForm(request.POST or None)
    if fwcons['numberofcoldcutsbaseform'].is_valid():
        fwcons['numberofcoldcutsbaseform'].save()
        flamgerimanhours = {

        }

        return HttpResponseRedirect('/')
    else:
        print fwcons['numberofcoldcutsbaseform'].errors

    return render_to_response('numcoldcutsbase.html', fwcons, context_instance=RequestContext(request))


def getnumberofhotcuts(request):
    fwcons = dict()
    fwcons['numberofhotcutsbaseform'] = NumberOfHotCutsBaseForm(request.POST or None)
    if fwcons['numberofhotcutsbaseform'].is_valid():
        fwcons['numberofhotcutsbaseform'].save()
        flamgerimanhours = {

        }

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