#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base
from pages.page import PageRegion
from pages.tasks.task_details import TaskDetailsPage


class AvailableTasksPage(Base):

    _page_title = 'Tasks | Mozilla One and Done'

    _available_tasks_list_locator = (By.CSS_SELECTOR, '.task-list > li')
    _displayed_profile_name_locator = (By.CSS_SELECTOR, '.content-container > h3')

    @property
    def available_tasks(self):
        return [self.Task(self.testsetup, web_element)
                for web_element in self.selenium.find_elements(*self._available_tasks_list_locator)]

    @property
    def displayed_profile_name(self):
        return self.selenium.find_element(*self._displayed_profile_name_locator).text

    class Task(PageRegion):
        _name_locator = (By.CSS_SELECTOR, 'a.task-name')

        @property
        def name(self):
            return self.find_element(*self._name_locator).text

        def click(self):
            self.find_element(*self._name_locator).click()
            return TaskDetailsPage(self.testsetup)
