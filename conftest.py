#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from mocks.mock_user import MockUser
from utils.oneanddone_api import OneAndDoneAPI


@pytest.fixture(scope='function')
def new_user(request):
    personatestuser_uri = 'http://personatestuser.org/email'

    # Request TestUser credentials from http://personatestuser.org
    response = requests.get(personatestuser_uri)

    testuser = response.json()
    request.new_user = MockUser(email=testuser['email'], password=testuser['pass'])

    def fin():
        # Delete user from application database after the test
        if request.new_user:
            mozwebqa = request.getfuncargvalue('mozwebqa')
            credentials = mozwebqa.credentials['default']
            api = OneAndDoneAPI(credentials['api_token'], mozwebqa.base_url)
            api.delete_user(request.new_user)

    request.addfinalizer(fin)
    return request.new_user
