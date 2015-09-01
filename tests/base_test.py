#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage


class BaseTest:

    def login_new_user(self, mozwebqa, user):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        assert not home_page.is_user_logged_in

        edit_profile = home_page.login(user)
        assert edit_profile.is_the_current_page
        assert edit_profile.is_user_logged_in

        edit_profile.type_name(user['name'])
        edit_profile.type_username(user['name'])
        assert edit_profile.is_privacy_policy_checkbox_checked
        home_page = edit_profile.click_save_button('home_page')
        return home_page
