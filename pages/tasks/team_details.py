# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class TeamDetailsPage(Base):

    _page_heading = (By.CSS_SELECTOR, '.content-container > h2')

    @property
    def page_heading(self):
        return self.selenium.find_element(*self._page_heading).text
