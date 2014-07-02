#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import requests

from unittestzero import Assert


class OneAndDoneAPI:

    def __init__(self, api_token, base_url):
        self.base_url = base_url
        self.token_authorization = 'Token %s' % (api_token)
        self.headers = {'Authorization': self.token_authorization,
                        'Content-Type': 'application/json'}

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

    def _do_post(self, uri, post_data, return_response_text=False):
        """Post to an API method and return the resulting id and the response text."""
        response = requests.post(
            "%s/%s/" % (self.base_url, uri),
            data=json.dumps(post_data),
            headers=self.headers)
        response.raise_for_status()
        text = json.loads(response.text)

        if response.status_code == 201:
            if return_response_text:
                return text['id'], text
            else:
                return text['id']
        else:
            print "Failed to create resource: %s with %s.\n%s" % (
                post_data, response.status_code, response.text)
            return None

    def delete_user(self, user):
        uri = 'api/v1/user'
        Assert.true(self._do_delete(uri, user['email']), 'Deletion of user with email %s failed' % user['email'])

    def create_user(self, user):
        uri = 'api/v1/user'
        post_data = {
            u'username': unicode(user['username']),
            u'email': unicode(user['email']),
            u'profile': {u'name': unicode(user['profile']['name'])}
        }
        user['id'], response_text = self._do_post(uri, post_data, True)
        user['profile']['name'] = response_text['profile']['name']
        Assert.greater(user['id'], 0, 'No user was created.')
        return user
