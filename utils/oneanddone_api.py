#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json

from unittestzero import Assert
import requests


class OneAndDoneAPI:

    def __init__(self, api_token, base_url):
        self.base_url = base_url
        self.token_authorization = 'Token %s' % (api_token)
        self.headers = {'Authorization': self.token_authorization}

    def _do_delete(self, uri, lookup_field):
        """Make a Delete Request"""
        response = requests.delete(
            '%s/%s/%s/' % (self.base_url, uri, lookup_field),
            headers=self.headers)

        response.raise_for_status()
        if response.status_code == 204:
            return True
        else:
            print "Failed to delete resource: %s with %s.\n%s" % (
                lookup_field, response.status_code, response.text)
            return False

    def delete_user(self, user):
        uri = 'api/v1/user'
        Assert.true(self._do_delete(uri, user['email']), 'Deletion of user with email %s failed' % user['email'])
