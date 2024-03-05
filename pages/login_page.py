import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    EMAIL_INPUT = ("name", "email")
    PASSWORD_INPUT = ("name", "password")
    LOGIN_SUBMIT_BUTTON = ("xpath", "//form//button[@type='submit']")


    @allure.step("Enter email")
    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(email)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(password)

    @allure.step("Click Login button")
    def click_login_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_SUBMIT_BUTTON)).click()