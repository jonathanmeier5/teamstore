from django.utils.http import urlencode
from django.core.urlresolvers import reverse
from .models import TeamStore


def reverseMod(*args, **kwargs):
	kwarg_d = kwargs['kwargs']
	get = kwarg_d.pop('get',{})
	url = reverse(*args, **kwargs)
	if 'team' in get:
		params = "?%s=%s" % ('team',get['team'])
		url += params
	return url


def get_team(team_name):
	  team = TeamStore.objects.filter(team_name=team_name).first()
	  return team

