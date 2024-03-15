import pytest
import allure
from config.data import Data
from pages.login_page import LoginPage
from pages.candidate_page import CandidatePage
from pages.candidate_edit_page import CandidateEditPage


class BaseTest:

    data: Data
    login_page: LoginPage
    candidate_page: CandidatePage
    candidate_edit_page: CandidateEditPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.candidate_page = CandidatePage(driver)
        request.cls.candidate_edit_page = CandidateEditPage(driver)