#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import datetime

class MockUser(dict):

    def __init__(self, **kwargs):

        now = str(datetime.datetime.now())
        self['id'] = None
        self['email'] = 'testuser@mozwebqa.com'
        self['password'] = 'p@ssw0rd'
        self['profile'] = {'name': 'MozWebQA User- ' + now,
                           'username': 'mozwebqauser%s' % now.split()[0],
                           'privacy_policy_accepted': False}

        self.update(**kwargs)

    def ___getattr__(self, attr):
        return self[attr]
