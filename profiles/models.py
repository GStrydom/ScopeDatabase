from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from clients.models import Client


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(Client)
    profilepic = models.CharField(max_length=255, blank=True, default=u"i like eggs")

    # Holds specific user id information such as Sapref badge number
    usercode = models.CharField(max_length=20, blank=True, default=u'Peaches and Cream')

    def __unicode__(self):
        return self.profilepic