from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from .models import Pipingnorms, FieldWeldsBase
from .models import SpadingNorms

from workpacks.models import Workpack


def createestimates(request):
    context = {}
    context.update(csrf(request))
    context['workpacks'] = Workpack.objects.all()

    return render_to_response('estimates.html', context, context_instance=RequestContext(request))


def getfieldweldbase(request):
    context = dict()

    return render_to_response('addfieldweld.html', context, context_instance=RequestContext(request))


def getdemolengthbase(request):
    context = dict()

    return render_to_response('adddemolength.html', context, context_instance=RequestContext(request))


def getinstalllengthbase(request):
    context = dict()

    return render_to_response('addinstalllength.html', context, context_instance=RequestContext(request))


def getflangeptbase(request):
    fwcons = dict()

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

    return render_to_response('flangeptbase.html', fwcons, context_instance=RequestContext(request))


def getflangeribase(request):
    fwcons = dict()

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

    return render_to_response('flangeribase.html', fwcons, context_instance=RequestContext(request))


def calcnumberofjoints(formobj, pipenorm):

    boltupnorm = pipenorm.objects.filter(pipediameter__exact=formobj.cleaned_data['diameter_id'])[0].boltupjointnormhours
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
    fwcons = dict()

    return render_to_response('addcoldcut.html', fwcons, context_instance=RequestContext(request))


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

    return render_to_response('addhotcut.html', fwcons, context_instance=RequestContext(request))