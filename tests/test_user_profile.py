#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import re

from pages.home import HomePage

from unittestzero import Assert
import pytest


class TestUserProfile:

    @pytest.mark.credentials
    def test_that_user_can_delete_profile(self, mozwebqa, existing_user):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.false(home_page.is_user_logged_in)

        logged_in_home_page = home_page.login(existing_user, 'home_page')
        Assert.true(logged_in_home_page.is_the_current_page)
        Assert.true(logged_in_home_page.is_user_logged_in)

        # click user profile details link
        user_profile_details_page = logged_in_home_page.header.click_user_profile_details()
        Assert.true(user_profile_details_page.is_the_current_page)

        # click edit profile button
        user_profile_edit_page = user_profile_details_page.click_edit_profile_button()
        Assert.true(user_profile_edit_page.is_the_current_page)

        # click delete profile button
        user_profile_delete_page = user_profile_edit_page.click_delete_profile_button()
        Assert.true(user_profile_delete_page.is_the_current_page)

        # click cancel button
        logged_in_home_page_after_cancel_deletion = user_profile_delete_page.click_cancel_button()
        Assert.true(logged_in_home_page_after_cancel_deletion.is_the_current_page)
        Assert.true(logged_in_home_page_after_cancel_deletion.is_user_logged_in)
        Assert.true(existing_user['profile']['name'].upper() in logged_in_home_page_after_cancel_deletion.header.profile_link_text)
        Assert.true(existing_user['profile']['name'] in logged_in_home_page_after_cancel_deletion.displayed_profile_name)

        # navigate back to the delete profile screen
        user_profile_details_page_after_cancel_deletion = logged_in_home_page_after_cancel_deletion.header.click_user_profile_details()
        user_profile_edit_page_after_cancel_deletion = user_profile_details_page_after_cancel_deletion.click_edit_profile_button()
        user_profile_delete_page_after_cancel_deletion = user_profile_edit_page_after_cancel_deletion.click_delete_profile_button()

        # click confirm button
        home_page_after_profile_deletion = user_profile_delete_page_after_cancel_deletion.click_confirm_button()
        Assert.false(home_page_after_profile_deletion.is_user_logged_in)

        # click login link
        create_profile_page = home_page_after_profile_deletion.login(existing_user, 'user_profile')
        Assert.true(create_profile_page.is_user_logged_in)
        Assert.true(create_profile_page.is_the_current_page)

    @pytest.mark.credentials
    def test_that_user_can_edit_profile(self, mozwebqa, existing_user):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.false(home_page.is_user_logged_in)

        logged_in_home_page = home_page.login(existing_user, 'home_page')
        Assert.true(logged_in_home_page.is_the_current_page)
        Assert.true(logged_in_home_page.is_user_logged_in)

        # click user profile details link
        user_profile_details_page = logged_in_home_page.header.click_user_profile_details()
        Assert.true(user_profile_details_page.is_the_current_page)

        # click edit profile button
        user_profile_edit_page = user_profile_details_page.click_edit_profile_button()
        Assert.true(user_profile_edit_page.is_the_current_page)
        Assert.equal(existing_user['profile']['name'], user_profile_edit_page.display_name)
        Assert.equal(existing_user['profile']['username'], user_profile_edit_page.username)

        # change display name and username
        new_display_name = re.sub(r'[\W_]+', '', existing_user['profile']['name'] + str(time.time()))
        new_username = re.sub(r'[\W_]+', '', existing_user['profile']['username'] + str(time.time()))
        user_profile_edit_page.enter_name(new_display_name)
        user_profile_edit_page.enter_username(new_username)
        home_page = user_profile_edit_page.click_save_button()

        Assert.true(home_page.is_the_current_page)
        Assert.true(new_display_name.upper() in home_page.header.profile_link_text)
        Assert.true(new_display_name in home_page.displayed_profile_name)

        # navigate to edit profile page
        user_profile_edit_page = home_page.header.click_user_profile_details().click_edit_profile_button()
        Assert.equal(new_display_name, user_profile_edit_page.display_name)
        Assert.equal(new_username, user_profile_edit_page.username)
