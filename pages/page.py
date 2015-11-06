# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    """
    Base class for all Pages
    """

    def __init__(self, base_url, selenium):
        """
        Constructor
        """
        self.base_url = base_url
        self.selenium = selenium
        self.timeout = 10
        self._selenium_root = hasattr(self, '_root_element') and self._root_element or self.selenium

    @property
    def is_the_current_page(self):
        WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
        assert self._page_title == self.selenium.title
        return True

    @property
    def current_page_url(self):
        return self.selenium.current_url

    def is_element_present(self, *locator):
        self.selenium.implicitly_wait(0)
        try:
            self._selenium_root.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.timeout)

    def is_element_visible(self, *locator):
        try:
            return self._selenium_root.find_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException):
            return False

    def is_element_not_visible(self, *locator):
        self.selenium.implicitly_wait(0)
        try:
            return not self._selenium_root.find_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            return True
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.timeout)

    def wait_for_element_visible(self, *locator):
        count = 0
        while not self.is_element_visible(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout:
                raise Exception(':'.join(locator) + ' is not visible')

    def wait_for_element_present(self, *locator):
        """Wait for an element to become present."""
        self.selenium.implicitly_wait(0)
        try:
            WebDriverWait(self.selenium, 10).until(lambda s: self._selenium_root.find_element(*locator))
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.timeout)

    def wait_for_element_not_present(self, *locator):
        """Wait for an element to become not present."""
        self.selenium.implicitly_wait(0)
        try:
            WebDriverWait(self.selenium, 10).until(lambda s: len(self._selenium_root.find_elements(*locator)) < 1)
            return True
        except TimeoutException:
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.timeout)

    def type_in_element(self, locator, text):
        """
        Type a string into an element.

        This method clears the element first then types the string via send_keys.

        Arguments:
        locator -- a locator for the element
        text -- the string to type via send_keys

        """
        text_fld = self._selenium_root.find_element(*locator)
        text_fld.clear()
        text_fld.send_keys(text)

    def maximize_window(self):
        try:
            self.selenium.maximize_window()
        except WebDriverException:
            pass

    def find_element(self, *locator):
        return self._selenium_root.find_element(*locator)

    def find_elements(self, *locator):
        return self._selenium_root.find_elements(*locator)


class PageRegion(Page):

    def __init__(self, base_url, selenium, element):
        self._root_element = element
        Page.__init__(self, base_url, selenium)
