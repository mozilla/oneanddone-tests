#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.page import Page


class Base(Page):
    """
    Base class for global project specific functions
    """
    
    @property
    def is_signed_in(self):
        return not self.header.is_sign_in_visible

    @property
    def header(self):
        """Return the common Header region."""
        return self.HeaderRegion(self.testsetup)

    
    class HeaderRegion(Page):
        _browserid_login_locator = (By.CSS_SELECTOR, '.browserid-login > span')
        _logout_menu_item_locator = (By.CSS_SELECTOR, '.auth-menu > .browserid-logout')

        def click_sign_in(self):
            self.selenium.find_element(*self._browserid_login_locator).click()

        def click_sign_out(self):
            self.selenium.find_element(*self._logout_menu_item_locator).click()

        @property
        def is_sign_in_visible(self):
            return self.is_element_visible(*self._browserid_login_locator)
