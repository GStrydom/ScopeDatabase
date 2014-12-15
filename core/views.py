from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, HttpResponseRedirect

from workpacks.models import Workpack


def homepageview(request):
    context = dict()

    context['workpacks'] = Workpack.objects.all()

    # Check for the
    if request.method == 'POST':
        if 'itemname' not in request.POST:
            pass
        else:
            nameofitemclicked = request.POST['itemname']

    return render_to_response('home.html', context)