#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class UserProfileEditPage(Base):

    _page_title = 'User profile | Mozilla One and Done'

    _name_input_locator = (By.ID, 'id_name')
    _privacy_policy_checkbox_locator = (By.ID, 'id_privacy_policy_accepted')
    _save_button_locator = (By.CSS_SELECTOR, '.edit-profile > .actions-container > .button')

    @property
    def is_privacy_policy_checkbox_checked(self):
        return self.selenium.find_element(*self._privacy_policy_checkbox_locator).is_selected()

    def enter_name(self, fullname):
        self.type_in_element(self._name_input_locator, fullname)

    def toggle_privacy_policy_checkbox(self):
        self.selenium.find_element(*self._privacy_policy_checkbox_locator).click()

    def click_save_button(self):
        self.selenium.find_element(*self._save_button_locator).click()
        from pages.user.user_dashboard import UserDashboardPage
        return UserDashboardPage(self.testsetup)
