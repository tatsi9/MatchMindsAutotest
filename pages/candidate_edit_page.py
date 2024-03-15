import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CandidateEditPage(BasePage):

    PAGE_URL = Links.CANDIDATE_EDIT_PAGE

    FIRSTNAME_INPUT = ("id", "firstName")
    SAVE_BUTTON = ("xpath", "//button[text()='Save changes']")

    def change_firstname(self, new_firstname):
        with allure.step(f"Change firstname on {new_firstname}"):
            firstname_input = self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME_INPUT))
            firstname_input.clear()
            firstname_input.send_keys(new_firstname)
            self.firstname = new_firstname

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes have been successfully")
    def is_change_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRSTNAME_INPUT, self.firstname))