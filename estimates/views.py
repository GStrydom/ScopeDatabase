from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from .models import EstimateDefaults, Pipingnorms, Manhoursfactor, FieldWeldsBase, FieldWeldsHours

from workpacks.models import Workpack, Lineclasses
from materials.models import SizeList

from fractions import Fraction

from .forms import FieldWeldHoursForm


def createestimates(request):
    createestcons = {}
    createestcons.update(csrf(request))
    createestcons['workpacks'] = Workpack.objects.all()
    createestcons['fieldwelds'] = FieldWeldsBase.objects.all()

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


def getfieldwelds(request):
    fwcons = dict()
    fwcons['fieldweldsform'] = FieldWeldHoursForm(request.POST or None)
    if fwcons['fieldweldsform'].is_valid():
        fwcons['fieldweldsform'].save()
        return HttpResponseRedirect('/')
    else:
        print fwcons['fieldweldsform'].errors

    return render_to_response('newfieldweld.html', fwcons, context_instance=RequestContext(request))