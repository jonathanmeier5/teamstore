from django.utils.http import urlencode
from django.core.urlresolvers import reverse


def reverseMod(*args, **kwargs):
	get = kwargs.pop('get', {})
	print(*args,**kwargs)
	url = reverse(*args, **kwargs)
	print(url)
	if 'team' in get:
		params = "?%s=%s" ('team',get['team'])
		url += params
		print(url)
	return url

