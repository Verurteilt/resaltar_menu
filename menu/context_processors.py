from django.utils.safestring import mark_safe
from django.core.urlresolvers import resolve
from django.http import Http404


def tab(request):
  tabs = {
    'inicio': ('home', ),
    'nosotros': ('about', ),
  }
  try:
    path = resolve(request.path)
    for tab, nombre_urls in tabs.iteritems():
      if path.url_name in nombre_urls:
        return {tab.upper(): mark_safe('class="active"')}
  except Http404: pass
  return {}