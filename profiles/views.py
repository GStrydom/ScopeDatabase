from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm, UserForm

from projects.models import Project


@login_required(login_url='/')
def register(request):
    context = dict()
    context.update(csrf(request))
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            HttpResponseRedirect('/')
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm
        profile_form = UserProfileForm

    context['user_form'] = user_form
    context['profile_form'] = profile_form
    context['registered'] = registered

    context['projects'] = Project.objects.all()

    return render_to_response('register.html', context, context_instance=RequestContext(request))


def loginuser(request):
    context = {}
    context.update(csrf(request))
    if request.method == 'POST':
        username = request.POST['Email']
        password = request.POST['Password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponse('Invalid login details supplied.')
    else:
        return render_to_response('login.html', context)


def user_info(request):
    pass