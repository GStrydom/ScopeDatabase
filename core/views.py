from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from workpacks.models import Workpack
from materials.models import Lineclass11011
import json


def homepageview(request):
    context = dict()
    context.update(csrf(request))

    context['workpacks'] = Workpack.objects.all()

    if request.method == 'POST':

        if 'workpacknumber' not in request.POST:
            pass
        else:
            context['collectedworkpack'] = Workpack.objects.filter(workpacknumber__exact=request.POST['workpacknumber'])[0]
            return json.dumps({'workpacklinenumber': context['collectedworkpack'].workpacklinenumber})

        if 'lineclass' not in request.POST:
            pass
        else:
            lineclass = request.POST['lineclass']
            itemname = request.POST['itemname']
            diameter = request.POST['diameter']
            quantity = request.POST['quantity']
            itemtype = request.POST['name']


    context['lineclass11011'] = Lineclass11011.objects.all().distinct()

    return render_to_response('page1.html', context)