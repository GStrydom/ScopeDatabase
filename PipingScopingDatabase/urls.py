from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core import views

urlpatterns = patterns('',

                       url(r'^registration/$', 'profiles.views.register', name='register'),

                       url(r'^login$', 'profiles.views.loginuser', name='loginuser'),

                       url(r'^$', views.homepageview, name='homepage'),

                       url(r'^new-workpack/$', 'workpacks.views.createworkpack', name='createworkpack'),

                       url(r'^new-estimates/$', 'estimates.views.createestimates', name="createestimates"),

                       url(r'^workpacks/get/(?P<workpack_id>\d+)/$', 'workpacks.views.showworkpack',
                           name="showworkpack"),

                       url(r'deletepack/$', 'workpacks.views.deletepack', name="deletepack"),

                       url(r'editpack/$', 'workpacks.views.editworkpack', name="editpack"),

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

                       url(r'^newflangept/$', 'estimates.views.getflangeptbase', name='newflangept'),

                       url(r'^newflangeri/$', 'estimates.views.getflangeribase', name='newflangeri'),

                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += staticfiles_urlpatterns()