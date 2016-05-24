from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pages.basepage import BasePage
from pages.searchpage import SearchPage

class HomePage(BasePage):

    def __init__ (self, context):
        super().__init__(context)
        self.title = 'Безкоштовні оголошення OLX.ua від Slando: дошка оголошень України — купівля/продаж бу товарів на сайті OLX.ua'
        self.url = 'http://olx.ua'

    def input_search(self, search):
        self.driver.find_element_by_css_selector('input.queryfield').send_keys(search)

    def search(self):
        self.driver.find_element_by_id('submit-searchmain').click()




def test(context):
    settings_available = [1, 1, 1]
    context.driver = webdriver.Firefox()
    context.driver.get('http://   ')
    a = context.driver.find_elements_by_css_selector('.settings')
    k = [i.text for i in a]
    assert k in a