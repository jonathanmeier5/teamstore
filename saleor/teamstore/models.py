from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import pgettext_lazy

from ..userprofile.models import Address

@python_2_unicode_compatible
class TeamStore(models.Model):

    team_name = models.CharField(
        pgettext_lazy('TeamStore field', 'team name'), max_length=100)
    
    team_code = models.CharField(
        pgettext_lazy('TeamStore field', 'team code'), max_length=25)

    shipping_address = models.ForeignKey(
        Address, related_name='+',
        verbose_name=pgettext_lazy('TeamStore field', 'shipping address'))

'''Here we can inherit from TeamStore to create sport specific stores
that automatically populate a preset series of items

class TriTeamStore(TeamStore)
class CyclingTeamStore(TeamStore)

'''

# @python_2_unicode_compatible
# class AuthorizationKey(models.Model):
#     site_settings = models.ForeignKey(SiteSettings)
#     name = models.CharField(
#         pgettext_lazy('Authentiaction field', 'name'), max_length=20,
#         choices=AuthenticationBackends.BACKENDS)
#     key = models.TextField(pgettext_lazy('Authentication field', 'key'))
#     password = models.TextField(
#         pgettext_lazy('Authentication field', 'password'))

#     class Meta:
#         unique_together = (('site_settings', 'name'),)

#     def __str__(self):
#         return self.name

#     def key_and_secret(self):
#         return self.key, self.password
