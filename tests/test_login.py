# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from .base_test import BaseTest


class TestLogin(BaseTest):

    def test_that_a_new_user_can_login(self, mozwebqa, new_user):
        home_page = self.login_new_user(mozwebqa, new_user)

        assert new_user['name'].upper() in home_page.header.profile_link_text
        assert new_user['name'] in home_page.displayed_profile_name
