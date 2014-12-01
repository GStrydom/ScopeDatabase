from django.shortcuts import render

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

from .forms import CreateNewReinstateForm

from workpacks.models import Lineclass, Workpack
from reinstatement.models import Reinstatement
def createreinstatematlist(request):
    """
    Create a new prefabrication material item tied to the workpack.
    """
    createreinstatecons = dict()
    createreinstatecons['newreinstate'] = CreateNewReinstateForm(data=request.POST)

    if request.method == 'POST':
        if createreinstatecons['newreinstate'].is_valid():
            item = Lineclass.objects.get(itemname__icontains=createreinstatecons['newreinstate'].cleaned_data['matlist'],
                                         dn1__icontains=createreinstatecons['newreinstate'].cleaned_data['sizelist'],
                                         lineclassname__icontains=createreinstatecons['newreinstate']
                                         .cleaned_data['lineclasses'])

            savedform = createreinstatecons['newreinstate'].save()
            savedform.code = item.code
            savedform.save()
            return HttpResponseRedirect('/')

    createreinstatecons['workpacks'] = Workpack.objects.all()

    return render_to_response('newprefab.html', createreinstatecons, context_instance=RequestContext(request))


def editreinstateitem(request, reinstatement_id):
    editcons = dict()
    editcons['reinstate'] = Reinstatement.objects.get(reinstatement_id=reinstatement_id)
    editcons['editreinstateform'] = CreateNewReinstateForm(request.POST or None, instance=editcons['reinstate'])
    if editcons['editreinstateform'].is_valid():
        editcons['editreinstateform'].save()
        return HttpResponseRedirect('/')
    editcons['workpacks'] = Workpack.objects.all()

    return render_to_response('editreinstate.html', editcons, context_instance=RequestContext(request))
