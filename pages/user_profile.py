#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import Base


class UserProfilePage(Base):

    _page_title = 'User profile | Mozilla One and Done'

    _name_input_locator = (By.ID, 'id_name')
    _save_button_locator = (By.CSS_SELECTOR, '.edit-profile > .actions-container > .button')

    def enter_name(self, fullname):
        self.type_in_element(self._name_input_locator, fullname)

    def click_save_button(self):
        self.selenium.find_element(*self._save_button_locator).click()
        from pages.user_dashboard import UserDashboardPage
        return UserDashboardPage(self.testsetup)
