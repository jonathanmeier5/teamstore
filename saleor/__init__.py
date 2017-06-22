
__version__ = 'dev'

from django.template.defaulttags import URLNode
from django.utils.safestring import SafeText

old_render = URLNode.render
def new_render(cls, context):
  """ Override existing url method to use pluses instead of spaces
  """
  get = "?%s=%s" % ('team',context.get('team','none'))
  s = SafeText(get)

  return str(old_render(cls, context)) + get

URLNode.render = new_render