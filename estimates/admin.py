from django.contrib import admin

from .models import FieldWeldsBase, Pipingnorms, FieldWeldsHours, NumberOfColdCutsBase, NumberOfHotCutsBase
from .models import DemoLengthBase, InstallLengthBase, NumberOfJointsBase, SpadingNorms

admin.site.register(FieldWeldsBase)
admin.site.register(Pipingnorms)
admin.site.register(FieldWeldsHours)
admin.site.register(NumberOfColdCutsBase)
admin.site.register(NumberOfHotCutsBase)
admin.site.register(DemoLengthBase)
admin.site.register(InstallLengthBase)
admin.site.register(NumberOfJointsBase)
admin.site.register(SpadingNorms)