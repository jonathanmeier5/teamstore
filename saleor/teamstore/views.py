# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse

from .forms import AuthenticationForm
from .models import TeamStore
from .utils import reverseMod

@csrf_protect
@never_cache
def login(request, template_name='team-code-login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm):
    """Displays the login form and handles the login action."""

    '''redirect_to = _clean_redirect(request.REQUEST.get(redirect_field_name, ''))'''

    # If the user is already logged in, redirect him immediately.

    if not settings.DEBUG:
        if request.session.get('valid_team_code', False):
            redirect_to = reverseMod('core:home', kwargs = {'get':{'team':request.session['team']}})
            return HttpResponseRedirect(redirect_to)

    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():
            # Mark the user as logged in via his session data.
            request.session['valid_team_code'] = True

            #THIS IS VERY BAD. FIGURE OUT WHY ON EARTH form.cleaned_data gives us bullshit.
            #code = form.cleaned_data.get('password')
            code = request.POST.get('password')

            team = TeamStore.objects.filter(team_code=code).first()
            request.session['team'] = team.team_name
            redirect_to = reverseMod('core:home', kwargs = {'get':{'team':request.session['team']}})

            return HttpResponseRedirect(redirect_to)

    else:
        form = authentication_form(request)


    return render(request, template_name, {'form': form})

def _clean_redirect(redirect_to):
    """
    Perform a few security checks on the redirect destination.

    Copied from django.contrib.auth.views.login. It really should be split
    out from that.
    """
    # Light security check -- make sure redirect_to isn't garbage.
    if not redirect_to or ' ' in redirect_to:
        redirect_to = settings.LOGIN_REDIRECT_URL

    # Heavier security check -- redirects to http://example.com should 
    # not be allowed, but things like /view/?param=http://example.com 
    # should be allowed. This regex checks if there is a '//' *before* a
    # question mark.
    elif '//' in redirect_to and re.match(r'[^\?]*//', redirect_to):
            redirect_to = settings.LOGIN_REDIRECT_URL

    return redirect_to

