from django.utils.http import urlencode
from django.core.urlresolvers import reverse


def reverseMod(*args, **kwargs):
	kwarg_d = kwargs['kwargs']
	get = kwarg_d.pop('get',{})
	print(kwargs)
	print("hello",get,*args,kwargs)
	url = reverse(*args, **kwargs)
	if 'team' in get:
		params = "?%s=%s" % ('team',get['team'])
		url += params
		print(url)
	print(url)
	return url

