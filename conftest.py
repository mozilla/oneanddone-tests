#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from mocks.mock_user import MockUser
from utils.oneanddone_api import OneAndDoneAPI


@pytest.fixture
def persona_test_user():
    return requests.get('http://personatestuser.org/email').json()


@pytest.fixture
def api(request, variables):
    token = variables['apiToken']
    url = request.getfuncargvalue('mozwebqa').base_url
    return OneAndDoneAPI(token, url)


@pytest.fixture(scope='function')
def existing_user(request, new_user, api):
    new_user['profile'].update({
        'name': 'mozwebqa_testuser',
        'username': new_user['username'],
        'privacy_policy_accepted': True})
    return api.create_user(new_user)


@pytest.fixture(scope='function')
def new_user(request, persona_test_user, api):
    user = MockUser(
        email=persona_test_user['email'],
        username=persona_test_user['email'].split('@')[0],
        password=persona_test_user['pass'])

    def fin():
        api.delete_user(user)
    request.addfinalizer(fin)
    return user
