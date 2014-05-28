#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage
from pages.user_profile import UserProfilePage

from unittestzero import Assert
import pytest


class TestLogin:

    @pytest.mark.credentials
    def test_that_a_new_user_can_login(self, mozwebqa, new_user):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.false(home_page.is_user_logged_in)

        user_profile_page = home_page.login(new_user, 'user_profile')
        Assert.true(user_profile_page.is_the_current_page)
        Assert.true(user_profile_page.is_user_logged_in)

        user_profile_page.enter_name(new_user['fullname'])
        user_profile_page.click_save_button()

        Assert.true(new_user['fullname'] in home_page.header.diplayed_text)
