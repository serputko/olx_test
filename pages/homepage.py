from pages.basepage import BasePage
from selenium import webdriver
from pages.locators import HomePage as hp
from pages.loginpage import LoginPage
from pages.searchpage import SearchPage


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
