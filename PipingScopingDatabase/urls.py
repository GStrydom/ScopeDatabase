from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core import views

urlpatterns = patterns('',

                       url(r'^registration/$', 'profiles.views.register', name='register'),

                       url(r'^users/$', 'core.views.userslist', name='userslist'),

                       url(r'^exportbom/$', 'core.views.exportbom', name='exportbom'),

                       url(r'^$', 'profiles.views.loginuser', name='loginuser'),

                       url(r'^home/$', views.homepageview, name='homepage'),

                       url(r'^new-workpack/$', 'workpacks.views.createworkpack', name='createworkpack'),

                       url(r'^workpacks/get/(?P<workpack_id>\d+)/$', 'workpacks.views.showworkpack',
                           name="showworkpack"),

                       url(r'deletepack/$', 'workpacks.views.deletepack', name="deletepack"),

                       url(r'editpack/(?P<workpack_id>\d+)/$', 'workpacks.views.editworkpack', name="editpack"),

                       url(r'^newfieldweld/', 'estimates.views.getfieldweldbase', name='getfieldweldbase'),

                       url(r'^newdemolength/$', 'estimates.views.getdemolengthbase', name='newdemolength'),

                       url(r'^newinstalllength/$', 'estimates.views.getinstalllengthbase', name='newinstalllength'),

                       url(r'^newnumjoints/$', 'estimates.views.getnumberofjoints', name='newnumjoints'),

                       url(r'^newcoldcuts/$', 'estimates.views.getnumberofcoldcuts', name='newcoldcuts'),

                       url(r'^newhotcuts/$', 'estimates.views.getnumberofhotcuts', name='newhotcuts'),

                       url(r'^newflangept/$', 'estimates.views.getflangeptbase', name='newflangept'),

                       url(r'^newflangeri/$', 'estimates.views.getflangeribase', name='newflangeri'),

                       url(r'^prefabs/$', 'materials.views.showprefabitems', name='showprefabs'),
                       url(r'^create-prefab/$', 'materials.views.createprefabitem', name='createprefab'),
                       url(r'^edit-prefab/(?P<materialitem_id>\d+)/$', 'materials.views.editprefabitem',
                           name='editprefab'),
                       url(r'^delete-prefab/(?P<materialitem_id>\d+)/$', 'materials.views.deleteprefabitem',
                           name='deleteprefab'),

                       url(r'^reinstates/$', 'materials.views.showreinstateitems', name='showreinstates'),
                       url(r'^create-reinstate/$', 'materials.views.createreinstateitem', name='createreinstates'),

                       url(r'^spadings/$', 'materials.views.showspadingitems', name='showspadings'),

                       url(r'^estimates/$', 'estimates.views.displayestimates', name='createestimates'),

                       url(r'^admin/', include(admin.site.urls))
                       )

urlpatterns += staticfiles_urlpatterns()