"""
Test utilities related to Request objects.
"""

from __future__ import absolute_import, unicode_literals

import crum

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory


def get_mock_request(user=None):
    """
    Create a request object for the user, if specified.
    """
    request = RequestFactory().get('/')
    if user is not None:
        request.user = user
    else:
        request.user = AnonymousUser()
    request.is_secure = lambda: True
    request.get_host = lambda: "edx.org"
    crum.set_current_request(request)
    return request
