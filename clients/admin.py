from django.contrib import admin

from .models import Client, Clientinformation

admin.site.register(Clientinformation)
admin.site.register(Client)
