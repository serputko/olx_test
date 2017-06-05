from pages.basepage import BasePage
from pages.locators import LoginPage as lp
from pages.profilepage import ProfilePage
from utils import utils


class LoginPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.title = 'Оголошення OLX.ua: дошка оголошень України — купівля/продаж бу товарів на сайті OLX.ua, раніше Slando'
        self.url = 'https://www.olx.ua/uk/account/'

    def login(self):
        credentials = utils.get_valid_credentials()
        self.driver.find_element(*lp.LOGIN_FIELD).send_keys(credentials['User'])
        self.driver.find_element(*lp.PASSWORD_FIELD).send_keys(credentials['Password'])
        self.driver.find_element(*lp.LOGIN_BUTTON).click()
        return ProfilePage(self)
