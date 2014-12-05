from django.contrib import admin

from .models import FieldWeldsBase, Pipingnorms, FieldWeldsHours

admin.site.register(FieldWeldsBase)
admin.site.register(Pipingnorms)
admin.site.register(FieldWeldsHours)