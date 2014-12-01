from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, HttpResponseRedirect

from workpacks.models import Workpack


def homepageview(request):
    homecons = dict()
    homecons['workpacks'] = Workpack.objects.all()
    return render_to_response('home.html', homecons)