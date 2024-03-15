import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CandidatePage(BasePage):

    PAGE_URL = Links.CANDIDATE_PAGE

    EDIT_PROFILE_LINK = ("xpath", "//a[contains(text(), 'Edit my profile')]")

    @allure.step("Click 'Edit profile' link")
    def click_edit_profile_link(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_PROFILE_LINK)).click()