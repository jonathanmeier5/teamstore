# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .models import TeamStore 

class AuthenticationForm(forms.Form):
    """
    Simple form to allow users to access a page via a password.

    A copy of django.contrib.auth.forms.AuthenticationForm, adapted to this
    much simpler use case.
    """
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        super(AuthenticationForm, self).__init__(*args, **kwargs)


    def clean_password(self):
        """
        Validate that the password entered was correct.
        """
        password = self.cleaned_data.get('password')
        team_qs = TeamStore.objects.filter(team_code=password)

        if team_qs.exists():
            correct_password = True
        else:
            correct_password = False

        print(correct_password)

        if not correct_password:
            raise forms.ValidationError(_("Invalid Team Code. Note that the code is case-sensitive."))

        # TODO: determine whether this should move to its own method.
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError(_("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in."))

        return self.cleaned_data

