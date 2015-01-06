from django.db import models
from django.contrib.auth.models import User

from clients.models import Client


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    company = models.ForeignKey(Client)
    profilepic = models.CharField(max_length=255, blank=True, null=True)

    # Holds specific user id information such as Sapref badge number
    usercode = models.CharField(max_length=20, blank=True, null=True)
    usertype = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.profilepic