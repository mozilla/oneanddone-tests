#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage

from unittestzero import Assert
import pytest


class TestUserTasks:

    @pytest.mark.credentials
    def test_that_user_can_complete_a_task(self, mozwebqa, existing_user):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.false(home_page.is_user_logged_in)

        user_dashboard_page = home_page.login(existing_user, 'user_dashboard')
        Assert.true(user_dashboard_page.is_the_current_page)
        Assert.true(user_dashboard_page.is_user_logged_in)

        # click available task button
        available_tasks_page = user_dashboard_page.click_pick_a_task_button()
        Assert.true(available_tasks_page.is_the_current_page)
        Assert.greater(len(available_tasks_page.available_tasks), 0)

        # select first available task from list
        selected_task_name = available_tasks_page.available_tasks[0].name
        task_details_page = available_tasks_page.available_tasks[0].click()
        Assert.true(task_details_page.is_the_current_page)
        Assert.true(task_details_page.is_get_started_button_visible)
        Assert.true(task_details_page.is_save_for_later_button_not_visible)
        Assert.true(task_details_page.is_abandon_task_button_not_visible)
        Assert.true(task_details_page.is_complete_task_button_not_visible)

        # click get started button
        task_details_page.click_get_started_button()
        Assert.true(task_details_page.is_the_current_page)
        Assert.true(task_details_page.is_get_started_button_not_visible)
        Assert.true(task_details_page.is_save_for_later_button_visible)
        Assert.true(task_details_page.is_abandon_task_button_visible)
        Assert.true(task_details_page.is_complete_task_button_visible)

        # click save for later button
        updated_user_dashboard_page = task_details_page.click_save_for_later_button()
        Assert.true(updated_user_dashboard_page.is_the_current_page)

        # click on task in progress
        Assert.true(updated_user_dashboard_page.is_task_in_progress)
        Assert.equal(updated_user_dashboard_page.task_in_progress, selected_task_name)
        task_in_progress_detail_page = updated_user_dashboard_page.click_task_in_progress()
        Assert.true(task_in_progress_detail_page.is_the_current_page)

        # click complete task button
        task_feedback_page = task_in_progress_detail_page.click_complete_task_button()
        Assert.true(task_feedback_page.is_the_current_page)

        # click no thanks button
        user_dashboard_after_task_completion = task_feedback_page.click_no_thanks_button()

        # click user profile details link
        user_profile_details_page = user_dashboard_after_task_completion.header.click_user_profile_details()
        Assert.true(user_profile_details_page.is_the_current_page)

        Assert.equal(user_profile_details_page.diplayed_completed_tasks_count, 1)
        Assert.equal(len(user_profile_details_page.completed_tasks), 1)
        Assert.equal(user_profile_details_page.completed_tasks[0].name, selected_task_name)

    @pytest.mark.credentials
    def test_that_user_can_abandon_a_task(self, mozwebqa, existing_user):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.false(home_page.is_user_logged_in)

        user_dashboard_page = home_page.login(existing_user, 'user_dashboard')
        Assert.true(user_dashboard_page.is_the_current_page)
        Assert.true(user_dashboard_page.is_user_logged_in)

        # click available task button
        available_tasks_page = user_dashboard_page.click_pick_a_task_button()
        Assert.true(available_tasks_page.is_the_current_page)
        Assert.greater(len(available_tasks_page.available_tasks), 0)

        # select first available task from list
        selected_task_name = available_tasks_page.available_tasks[0].name
        task_details_page = available_tasks_page.available_tasks[0].click()
        Assert.true(task_details_page.is_the_current_page)

        # click get started button
        task_details_page.click_get_started_button()
        Assert.true(task_details_page.is_the_current_page)

        # click abandon task button
        task_feedback_page = task_details_page.click_abandon_task_button()
        Assert.true(task_feedback_page.is_the_current_page)
        Assert.equal(task_feedback_page.name, selected_task_name)

        # click no thanks button
        user_dashboard_after_abandon_task = task_feedback_page.click_no_thanks_button()
        Assert.true(user_dashboard_after_abandon_task.is_the_current_page)
        Assert.true(user_dashboard_after_abandon_task.is_task_not_in_progress)

        # click user profile details link
        user_profile_details_page = user_dashboard_after_abandon_task.header.click_user_profile_details()
        Assert.true(user_profile_details_page.is_the_current_page)

        Assert.equal(user_profile_details_page.diplayed_completed_tasks_count, 0)
