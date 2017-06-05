from pages.basepage import BasePage
from pages.locators import LoginPage as lp


class ProfilePage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.title = 'Мій профіль • OLX.ua'
        self.url = 'https://www.olx.ua/uk/myaccount/#login'
