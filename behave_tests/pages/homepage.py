from behave_tests.pages.basepage import BasePage
from behave_tests.pages.locators import HomePage as hp
from behave_tests.pages.searchpage import SearchPage

from behave_tests.pages.loginpage import LoginPage


class HomePage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.title = 'Безкоштовні оголошення OLX.ua від Slando: дошка оголошень України — купівля/продаж бу товарів на сайті OLX.ua'
        self.url = 'http://olx.ua'

    def input_search(self, search):
        self.driver.find_element(*hp.INPUT_FIELD).send_keys(search)

    def search(self):
        self.driver.find_element(*hp.SEARCH_BUTTON).click()
        return SearchPage(self)

    def open_login_page(self):
        self.driver.find_element(*hp.PROFILE_BUTTON).click()
        return LoginPage(self)
