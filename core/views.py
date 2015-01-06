from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from workpacks.models import Workpack
from materials.models import Lineclass11011


def homepageview(request):
    context = dict()
    context.update(csrf(request))

    context['workpacks'] = Workpack.objects.all()

    context['lineclass11011'] = Lineclass11011.objects.all().distinct()

    return render_to_response('home.html', context)