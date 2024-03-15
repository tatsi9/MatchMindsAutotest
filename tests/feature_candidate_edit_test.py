import random
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Profile functionality")
class TestCandidateFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_firstname(self):
        self.login_page.open(self)
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_submit_button()
        self.candidate_page.is_opened()
        self.candidate_page.click_edit_profile_link()
        self.candidate_edit_page.is_opened()
        self.candidate_edit_page.change_firstname(f"Test {random.randint(1, 100)}")
        self.candidate_edit_page.save_changes()
        self.candidate_edit_page.is_change_saved()
        self.candidate_edit_page.make_screenshot("Success_screenshots")



