from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from .models import EstimateDefaults, Pipingnorms, Manhoursfactor, FieldWeldsBase, FieldWeldsHours
from .models import DemoLengthBase, SpadingNorms

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

    if request.method == 'POST':
        grindprepresource = request.POST['resource']
        print grindprepresource

    createestcons['opsverify'] = {
        'duration': 1,
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

    totalgrindprep = int(math.ceil(totalGrindPrep))
    totalweldweld = int(math.ceil(totalWeldWeld))
    totalweldfit = int(math.ceil(totalWeldFit))

    createestcons['fieldweldbase'] = {
        'totalgrindprep': totalgrindprep,
        'totalweldweld': totalweldweld,
        'totalweldfit': totalweldfit
    }

    createestcons['qcfitupcheck'] = {
        'resources': 1,
        'manhours': totalQcFitUpCheck,
        'duration': totalQcFitUpCheck
    }

    createestcons['demolengthbase'] = {
        'totalrigoutlinerig': int(math.ceil(totalRigOutLineRig)),
        'totalrigoutlinefit': int(math.ceil(totalRigOutLineFit))
    }

    createestcons['installlengthbase'] = {
        'totalrigInlinerig': math.ceil(totalRigInLineRig),
        'totalrigInlinefit': math.ceil(totalRigInLineFit)
    }

    createestcons['numberofjointsbase'] = {
        'totalunboltjointsfitter': math.ceil(totalUnboltJointsFitter),
        'totalboltupjointsfitter': math.ceil(totalBoltUpJointsFitter)
    }

    createestcons['coldcutsbase'] = {
        'totalcoldcutline': math.ceil(totalColdCutLine)
    }

    createestcons['hotcutsbase'] = {
        'totalhotcutline': math.ceil(totalHotCutLine)
    }

    createestcons['totals'] = {
    }

    return render_to_response('estimates.html', createestcons, context_instance=RequestContext(request))


totalGrindPrep = 0
totalWeldWeld = 0
totalWeldFit = 0
totalFieldWelds = 0
totalQcFitUpCheck = 0


def getfieldweldbase(request):
    fwcons = dict()
    global totalGrindPrep
    global totalWeldWeld
    global totalWeldFit
    global totalFieldWelds
    global totalQcFitUpCheck
    schedule40 = [1.5, 1, 2, 3, 4, 6]
    fwcons['fieldweldsbaseform'] = FieldWeldsBaseForm(request.POST or None)
    if fwcons['fieldweldsbaseform'].is_valid():
        savedform = fwcons['fieldweldsbaseform'].save(commit=False)
        savedform.workpack_id = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        savedform.save()
        if fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'] in schedule40:
            grind1 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'])[0].cut
            grind2 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'])[0].prep
            grind3 = fwcons['fieldweldsbaseform'].cleaned_data['numberoffieldwelds']
            weld1 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'])[0].tackweldlesseighty
            fieldweldsduration = {
                'grindprep': (grind1 + grind2) * 2 * grind3 * 1,
                'weldweld': weld1 * grind3 * 1,
                'qcfitupcheck': 1 * grind3
            }

            totalQcFitUpCheck += grind3

            if fwcons['fieldweldsbaseform'].cleaned_data['diameter_id'] < 4:
                fieldweldsduration['weldfit'] = fieldweldsduration['weldweld'] * 0.15
            else:
                fieldweldsduration['weldfit'] = fieldweldsduration['weldweld'] * 0.3
            totalGrindPrep += fieldweldsduration['grindprep']
            totalWeldWeld += fieldweldsduration['weldweld']
            totalWeldFit += fieldweldsduration['weldfit']
            totalFieldWelds = totalGrindPrep + totalWeldFit + totalWeldWeld

            fwcons['fieldweldshoursform'] = FieldWeldHoursForm(request.POST or None)
            savedform = fwcons['fieldweldshoursform'].save(commit=False)
            savedform.manhours = ''

        return HttpResponseRedirect('/new-estimates/')
    else:
        print fwcons['fieldweldsbaseform'].errors

    return render_to_response('newfieldweld.html', fwcons, context_instance=RequestContext(request))


totalRigOutLineRig = 0
totalRigOutLineFit = 0
totalRigInLineRigdemo = 0
totalRigInLineFitdemo = 0


# TODO: Confirm rig in line with Juan
def getdemolengthbase(request):
    fwcons = dict()
    global totalRigOutLineRig
    global totalRigOutLineFit
    global totalRigInLineRigdemo
    global totalRigInLineFitdemo
    fwcons['demolengthbaseform'] = DemoLengthBaseForm(request.POST or None)
    if fwcons['demolengthbaseform'].is_valid():
        fwcons['demolengthbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['demolengthbaseform'].save()
        rig1 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['demolengthbaseform'].cleaned_data['diameter_id'])[0].handlemeternormshours
        rig2 = fwcons['demolengthbaseform'].cleaned_data['demolength']
        demolengthmanhours = {
            'rigoutlinerig': rig1 * rig2
        }

        demolengthmanhours['rigoutlinefit'] = demolengthmanhours['rigoutlinerig']
        # TODO: Check to remove riginlinedemo
        demolengthmanhours['riginlinerigdemo'] = demolengthmanhours['rigoutlinerig']
        demolengthmanhours['riginlinefitdemo'] = demolengthmanhours['rigoutlinerig']
        totalRigOutLineRig += demolengthmanhours['rigoutlinerig']
        totalRigOutLineFit += demolengthmanhours['rigoutlinefit']
        # TODO: Check to remove riginlinedemo
        totalRigInLineRigdemo += demolengthmanhours['riginlinerigdemo']
        totalRigInLineFitdemo += demolengthmanhours['riginlinefitdemo']

        print 'Demo Length Vars:'
        print 'Handle Meter Norms: %f' % rig1
        print 'Demo length: %f' % rig2

        print 'Demo length manhours riggers: '
        print 'Rig out line rigger: %f' % demolengthmanhours['rigoutlinerig']
        print 'Rig out line fitter: %f' % demolengthmanhours['rigoutlinefit']
        print 'Rig in line rigger demo: %f' % demolengthmanhours['riginlinerigdemo']
        print 'Rig in line fitter demo: %f' % demolengthmanhours['riginlinefitdemo']
        print
        print 'Total Rig In Line Rig Demo %f' % totalRigInLineRigdemo
        print 'Total Rig In Line Fit Demo %f' % totalRigInLineFitdemo

        return HttpResponseRedirect('/')
    else:
        print fwcons['demolengthbaseform'].errors

    return render_to_response('demolengthbase.html', fwcons, context_instance=RequestContext(request))


totalRigInLineRig = 0
totalRigInLineFit = 0


def getinstalllengthbase(request):
    global totalRigInLineRig
    global totalRigInLineFit
    fwcons = dict()
    fwcons['installlengthbaseform'] = InstallLengthBaseForm(request.POST or None)
    if fwcons['installlengthbaseform'].is_valid():
        fwcons['installlengthbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['installlengthbaseform'].save()
        rig1 = Pipingnorms.objects.filter(pipediameter__exact=fwcons['installlengthbaseform'].cleaned_data['diameter_id'])[0].handlemeternormshours
        rig2 = fwcons['installlengthbaseform'].cleaned_data['installlength']
        installlengthmanhours = {
            'riginlinerig': rig1 * rig2
        }

        installlengthmanhours['riginlinefit'] = installlengthmanhours['riginlinerig']

        totalRigInLineRig += installlengthmanhours['riginlinerig']
        totalRigInLineFit += installlengthmanhours['riginlinefit']

        return HttpResponseRedirect('/')
    else:
        print fwcons['installlengthbaseform'].errors

    return render_to_response('newinstalllength.html', fwcons, context_instance=RequestContext(request))

totalInstIso2 = 0


def getflangeptbase(request):
    fwcons = dict()
    global totalInstIso2
    fwcons['flangepressuretestbaseform'] = FlangePressureTestBaseForm(request.POST or None)
    if fwcons['flangepressuretestbaseform'].is_valid():
        fwcons['flangepressuretestbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['flangepressuretestbaseform'].save()

        if fwcons['flangepressuretestbaseform'].cleaned_data['flangehndlehotcut']:
            flgvar = 1 + SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'])[0].cuttingfactorhw - 1
        else:
            flgvar = 1

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

        instiso1 = fwcons['flangepressuretestbaseform'].cleaned_data['numfpt']
        instiso2 = SpadingNorms.objects.filter(sizes=fwcons['flangepressuretestbaseform'].cleaned_data['diameter_id'])[0].manhrs
        flangeptmanhours = {
            'installisoandpt': instiso1 * instiso2 * flgvar + alkyvar + hacksawvar + fambavar
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

totalUnboltJointsFitter = 0
totalBoltUpJointsFitter = 0
totalUnboltJointsRigger = 0
totalBoltupJointsRigger = 0
instrumentsBool = []


def getnumberofjoints(request):
    fwcons = dict()
    global totalUnboltJointsFitter
    global totalBoltUpJointsFitter
    global totalBoltupJointsRigger
    global totalUnboltJointsRigger
    global instrumentsBool

    fwcons['numberofjointsbaseform'] = NumberOfJointsBaseForm(request.POST or None)
    if fwcons['numberofjointsbaseform'].is_valid():
        fwcons['numberofjointsbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['numberofjointsbaseform'].save()
        boltupjointnorm = Pipingnorms.objects.filter(pipediameter__exact=fwcons['numberofjointsbaseform'].cleaned_data['diameter_id'])[0].boltupjointnormhours
        numjoints = fwcons['numberofjointsbaseform'].cleaned_data['numjoints']
        numjointsmanhours = {
            'unboltjointsfitter': numjoints * boltupjointnorm,
            'boltupjointsfitter': numjoints * boltupjointnorm
        }

        totalUnboltJointsFitter += numjointsmanhours['unboltjointsfitter']
        totalBoltUpJointsFitter += numjointsmanhours['boltupjointsfitter']

        if fwcons['numberofjointsbaseform'].cleaned_data['instrumentsboltup']:
            instrumentsBool.append(True)
        else:
            instrumentsBool.append(False)

        for boolval in instrumentsBool:
            if boolval:
                disconnectinstruments = 3
            else:
                disconnectinstruments = 0

        if fwcons['numberofjointsbaseform'].cleaned_data['rigforjoints']:
            riggersforunbolt = numjointsmanhours['unboltjointsfitter']
            riggersforboltup = numjointsmanhours['boltupjointsfitter']

            totalUnboltJointsRigger += riggersforunbolt
            totalBoltupJointsRigger += riggersforboltup

        return HttpResponseRedirect('/')
    else:
        print fwcons['numberofjointsbaseform'].errors

    return render_to_response('numjointsbase.html', fwcons, context_instance=RequestContext(request))

totalColdCutLine = 0
totalRiggersForColdCut = 0


def getnumberofcoldcuts(request):
    fwcons = dict()
    global totalColdCutLine
    global totalRiggersForColdCut
    fwcons['numberofcoldcutsbaseform'] = NumberOfColdCutsBaseForm(request.POST or None)
    if fwcons['numberofcoldcutsbaseform'].is_valid():
        fwcons['numberofcoldcutsbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['numberofcoldcutsbaseform'].save()
        coldcutnorm = Pipingnorms.objects.filter(pipediameter__exact=fwcons['numberofcoldcutsbaseform'].cleaned_data['diameter_id'])[0].coldcutnormhours
        numcuts = fwcons['numberofcoldcutsbaseform'].cleaned_data['numcoldcuts']
        coldcutmanhours = {
            'coldcutline': coldcutnorm * numcuts * 1
        }

        totalColdCutLine += coldcutmanhours['coldcutline']

        if fwcons['numberofcoldcutsbaseform'].cleaned_data['diameter_id'] >= 4:
            riggersforcoldcut = coldcutmanhours['coldcutline']
        else:
            riggersforcoldcut = 0
        request.session['rigforcoldcut'] = riggersforcoldcut

        totalRiggersForColdCut += riggersforcoldcut

        return HttpResponseRedirect('/')
    else:
        print fwcons['numberofcoldcutsbaseform'].errors

    return render_to_response('numcoldcutsbase.html', fwcons, context_instance=RequestContext(request))


totalHotCutLine = 0
totalRiggersForHotCut = 0


def getnumberofhotcuts(request):
    fwcons = dict()
    global totalHotCutLine
    global totalRiggersForHotCut
    fwcons['numberofhotcutsbaseform'] = NumberOfHotCutsBaseForm(request.POST or None)
    if fwcons['numberofhotcutsbaseform'].is_valid():
        fwcons['numberofhotcutsbaseform'].fields['workpack'] = Workpack.objects.get(workpack_id=request.session['workpackselected'])
        fwcons['numberofhotcutsbaseform'].save()
        hotcutnorm = Pipingnorms.objects.filter(pipediameter__exact=fwcons['numberofhotcutsbaseform'].cleaned_data['diameter_id'])[0].hotcutnormhours
        numcuts = fwcons['numberofhotcutsbaseform'].cleaned_data['numhotcuts']
        hotcutmanhours = {
            'hotcutline': hotcutnorm * numcuts * 1
        }

        totalHotCutLine += hotcutmanhours['hotcutline']

        if fwcons['numberofhotcutsbaseform'].cleaned_data['diameter_id'] >= 4:
            riggersforhotcut = hotcutmanhours['hotcutline']
        else:
            riggersforhotcut = 0
        request.session['rigforcoldcut'] = riggersforhotcut
        totalRiggersForHotCut += riggersforhotcut

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