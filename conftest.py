#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from mocks.mock_user import MockUser
from utils.oneanddone_api import OneAndDoneAPI


def get_personatestuser():
    # Request TestUser credentials from http://personatestuser.org
    personatestuser_uri = 'http://personatestuser.org/email'
    response = requests.get(personatestuser_uri)
    return response.json()


def delete_user_from_database(mozwebqa, user):
    credentials = mozwebqa.credentials['default']
    api = OneAndDoneAPI(credentials['api_token'], mozwebqa.base_url)
    api.delete_user(user)


def create_user_in_database(mozwebqa, user):
    credentials = mozwebqa.credentials['default']
    api = OneAndDoneAPI(credentials['api_token'], mozwebqa.base_url)
    return api.create_user(user)


@pytest.fixture(scope='function')
def existing_user(request):
    testuser = get_personatestuser()
    mozwebqa = request.getfuncargvalue('mozwebqa')
    request.existing_user = create_user_in_database(
        mozwebqa, MockUser(email=testuser['email'], password=testuser['pass']))

    def fin():
        # Delete user from application database after the test
        if request.existing_user:
            delete_user_from_database(mozwebqa, request.existing_user)

    request.addfinalizer(fin)
    return request.existing_user


@pytest.fixture(scope='function')
def new_user(request):
    testuser = get_personatestuser()
    request.new_user = MockUser(email=testuser['email'], password=testuser['pass'])

    def fin():
        # Delete user from application database after the test
        if request.new_user:
            mozwebqa = request.getfuncargvalue('mozwebqa')
            delete_user_from_database(mozwebqa, request.new_user)

    request.addfinalizer(fin)
    return request.new_user
