from django.contrib import admin

from .models import FieldWeldsBase, Pipingnorms, NumberOfColdCutsBase, NumberOfHotCutsBase
from .models import DemoLengthBase, InstallLengthBase, NumberOfJointsBase, SpadingNorms, FlangePressureTestBase
from .models import FlangeReinstateBase

admin.site.register(FieldWeldsBase)
admin.site.register(Pipingnorms)
admin.site.register(NumberOfColdCutsBase)
admin.site.register(NumberOfHotCutsBase)
admin.site.register(DemoLengthBase)
admin.site.register(InstallLengthBase)
admin.site.register(NumberOfJointsBase)
admin.site.register(SpadingNorms)
admin.site.register(FlangePressureTestBase)
admin.site.register(FlangeReinstateBase)