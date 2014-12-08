from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core import views

urlpatterns = patterns('',

                       url(r'^registration/$', 'profiles.views.register', name='register'),

                       # url(r'^login$', 'profiles.views.loginuser', name='loginuser'),

                       url(r'^$', views.homepageview, name='homepage'),

                       url(r'^new-workpack/$', 'workpacks.views.createworkpack', name='createworkpack'),

                       url(r'^new-prefab/$', 'prefabrication.views.createprefabmatlist', name='createprefab'),

                       url(r'^new-spading/$', 'spading.views.createspadematlist', name='createprefab'),

                       url(r'^new-reinstate/$', 'reinstatement.views.createreinstatematlist', name='createreinstate'),

                       url(r'^new-estimates/$', 'estimates.views.createestimates', name="createestimates"),

                       url(r'^workpacks/get/(?P<workpack_id>\d+)/$', 'workpacks.views.showworkpack',
                           name="showworkpack"),

                       url(r'showprefab/$', 'workpacks.views.showprefab', name='showprefab'),

                       url(r'showspade/$', 'workpacks.views.showspade', name='showspade'),

                       url(r'showreinstate/$', 'workpacks.views.showreinstate', name='showreinstate'),

                       url(r'deletepack/$', 'workpacks.views.deletepack', name="deletepack"),

                       url(r'editpack/$', 'workpacks.views.editworkpack', name="editpack"),

                       url(r'^prefabrication/get/(?P<prefabrication_id>\d+)/$', 'prefabrication.views.editprefabitem',
                           name='editprefab'),

                       url(r'^spading/get/(?P<spading_id>\d+)/$', 'spading.views.editspadeitem',
                           name='editspade'),

                       url(r'^newfieldweld/', 'estimates.views.getfieldweldbase', name='getfieldweldbase'),
                       url(r'^fieldwelds/get/(?P<fieldweld_id>\d+)/$', 'estimates.views.editfieldweld',
                           name="editfieldweld"),
                       url(r'^fieldwelds/delete/(?P<fieldweld_id>\d+)/$', 'estimates.views.deletefieldweld',
                           name="deletefieldweld"),

                       url(r'^newdemolength/$', 'estimates.views.getdemolengthbase', name='newdemolength'),

                       url(r'^newinstalllength/$', 'estimates.views.getinstalllengthbase', name='newinstalllength'),

                       url(r'^newnumjoints/$', 'estimates.views.getnumberofjoints', name='newnumjoints'),

                       url(r'^newcoldcuts/$', 'estimates.views.getnumberofcoldcuts', name='newcoldcuts'),

                       url(r'^newhotcuts/$', 'estimates.views.getnumberofhotcuts', name='newhotcuts'),

                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += staticfiles_urlpatterns()