#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import uuid

from .base_test import BaseTest


class TestUserProfile(BaseTest):

    def test_that_user_can_edit_and_delete_profile(self, mozwebqa, new_user):
        home_page = self.login_new_user(mozwebqa, new_user)

        profile_details = home_page.header.click_user_profile_details()
        edit_profile = profile_details.click_edit_profile_button()
        assert edit_profile.is_the_current_page
        assert new_user['name'] == edit_profile.display_name
        assert new_user['name'] == edit_profile.username

        new_name = str(uuid.uuid4())
        new_username = str(uuid.uuid4()).replace('-', '')[10:]
        edit_profile.type_name(new_name)
        edit_profile.type_username(new_username)
        edit_profile.type_user_profile_url(new_user['url'])
        edit_profile.type_bugzilla_email(new_user['email'])
        profile_details = edit_profile.click_save_button('user_profile_details')

        assert profile_details.is_the_current_page
        assert new_name == profile_details.user_profile_name
        assert new_user['url'] == profile_details.user_profile_url
        assert new_user['email'] == profile_details.bugzilla_email

        edit_profile = profile_details.click_edit_profile_button()
        assert new_name == edit_profile.display_name
        assert new_username == edit_profile.username
        assert new_user['url'] == edit_profile.user_profile_url
        assert new_user['email'] == edit_profile.bugzilla_email

        confirm_delete = edit_profile.click_delete_profile_button()
        assert confirm_delete.is_the_current_page

        homepage = confirm_delete.click_cancel_button()
        assert homepage.is_the_current_page
        assert homepage.is_user_logged_in
        assert new_name.upper() in homepage.header.profile_link_text
        assert new_name in homepage.displayed_profile_name

        profile_details = home_page.header.click_user_profile_details()
        edit_profile = profile_details.click_edit_profile_button()
        confirm_delete = edit_profile.click_delete_profile_button()
        home_page = confirm_delete.click_confirm_button()
        assert not home_page.is_user_logged_in

        create_profile = home_page.login(new_user)
        assert create_profile.is_user_logged_in
        assert create_profile.is_the_current_page
