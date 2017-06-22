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

    class Meta:
        verbose_name = pgettext_lazy('TeamStore model', 'teamstore')
        verbose_name_plural = pgettext_lazy('TeamStore models', 'teamstores')
        app_label = 'teamstore'

'''Here we can inherit from TeamStore to create sport specific stores
that automatically populate a preset series of items'''
