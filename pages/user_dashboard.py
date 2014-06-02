#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import Base


class UserDashboardPage(Base):

    _page_title = 'Mozilla One and Done'

    _displayed_profile_name_locator = (By.CSS_SELECTOR, '.content-container > h3')

    @property
    def displayed_profile_name(self):
        return self.selenium.find_element(*self._displayed_profile_name_locator).text
