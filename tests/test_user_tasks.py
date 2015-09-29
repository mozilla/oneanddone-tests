#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.home import HomePage


class TestUserTasks:

    @pytest.mark.credentials
    def test_that_user_can_complete_a_task(self, mozwebqa, existing_user):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        assert not home_page.is_user_logged_in

        logged_in_home_page = home_page.login(existing_user, 'home_page')
        assert logged_in_home_page.is_the_current_page
        assert logged_in_home_page.is_user_logged_in

        # click available task button
        available_tasks_page = logged_in_home_page.click_pick_a_task_button()
        assert available_tasks_page.is_the_current_page
        assert len(available_tasks_page.available_tasks) > 0

        # select first available task from list
        selected_task_name = available_tasks_page.available_tasks[0].name
        task_details_page = available_tasks_page.available_tasks[0].click()
        assert task_details_page.is_the_current_page
        assert task_details_page.is_get_started_button_visible
        assert task_details_page.is_save_for_later_button_not_visible
        assert task_details_page.is_abandon_task_button_not_visible
        assert task_details_page.is_complete_task_button_not_visible

        # click get started button
        task_details_page.click_get_started_button()
        assert task_details_page.is_the_current_page
        assert task_details_page.is_get_started_button_not_visible
        assert task_details_page.is_save_for_later_button_visible
        assert task_details_page.is_abandon_task_button_visible
        assert task_details_page.is_complete_task_button_visible

        # click save for later button
        updated_logged_in_home_page = task_details_page.click_save_for_later_button()
        assert updated_logged_in_home_page.is_the_current_page

        # click on task in progress
        assert updated_logged_in_home_page.is_task_in_progress
        assert selected_task_name == updated_logged_in_home_page.task_in_progress
        task_in_progress_detail_page = updated_logged_in_home_page.click_task_in_progress()
        assert task_in_progress_detail_page.is_the_current_page

        # click complete task button
        task_feedback_page = task_in_progress_detail_page.click_complete_task_button()
        assert task_feedback_page.is_the_current_page

        # click no thanks button
        logged_in_home_page_after_task_completion = task_feedback_page.click_no_thanks_button()

        # click user profile details link
        user_profile_details_page = logged_in_home_page_after_task_completion.header.click_user_profile_details()
        assert user_profile_details_page.is_the_current_page

        assert 1 == user_profile_details_page.diplayed_completed_tasks_count
        assert 1 == len(user_profile_details_page.completed_tasks)
        assert selected_task_name == user_profile_details_page.completed_tasks[0].name

    @pytest.mark.credentials
    def test_that_user_can_abandon_a_task(self, mozwebqa, existing_user):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        assert not home_page.is_user_logged_in

        logged_in_home_page = home_page.login(existing_user, 'home_page')
        assert logged_in_home_page.is_the_current_page
        assert logged_in_home_page.is_user_logged_in

        # click available task button
        available_tasks_page = logged_in_home_page.click_pick_a_task_button()
        assert available_tasks_page.is_the_current_page
        assert len(available_tasks_page.available_tasks) > 0

        # select first available task from list
        selected_task_name = available_tasks_page.available_tasks[0].name
        task_details_page = available_tasks_page.available_tasks[0].click()
        assert task_details_page.is_the_current_page

        # click get started button
        task_details_page.click_get_started_button()
        assert task_details_page.is_the_current_page

        # click abandon task button
        task_feedback_page = task_details_page.click_abandon_task_button()
        assert task_feedback_page.is_the_current_page
        assert selected_task_name == task_feedback_page.name

        # click no thanks button
        whats_next_page = task_feedback_page.click_no_thanks_button()
        assert whats_next_page.is_the_current_page

        # click user profile details link
        user_profile_details_page = whats_next_page.header.click_user_profile_details()
        assert user_profile_details_page.is_the_current_page

        assert 0 == user_profile_details_page.diplayed_completed_tasks_count
