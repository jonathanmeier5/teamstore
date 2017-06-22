from .models import TeamStore
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse
from django.utils.http import urlquote


class TeamStoreAuthMiddleware(object):

	def process_view(self, request, view_func, view_args, view_kwargs):

		valid_team_code = request.session.get('valid_team_code', False)

		if valid_team_code:
			return None

		if request.path == reverse('teamstore:login'):
			return None

		return HttpResponseRedirect(reverse('teamstore:login'))