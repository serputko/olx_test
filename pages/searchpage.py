import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage

class SearchPage(BasePage):

    def __init__ (self, context):
        super().__init__(context)
        self.title = 'Крокодил - OLX.ua'


    def select_category(self, category):
        self.driver.find_element_by_css_selector('div.combospace').click()
        self.list_of_categories = self.driver.find_elements_by_css_selector('#categorySelectList>li>a')
        self.items = [i.text for i in self.list_of_categories]
        for i, j in enumerate(self.items):
            if j.startswith(category):
                self.driver.find_element_by_css_selector('#categorySelectList>li:nth-child({})'.format(i+1)).click()



    def assert_results_consists(self, search):
        """
        offers = self.driver.find_elements_by_css_selector('#offers_table .offer .link strong')
        items = [i.text for i in offers]
        for i in items:
            assert i.find(search)
        """
        self.srch = search
        try:
            WebDriverWait(self.driver, 10).until(lambda b: b.find_element_by_css_selector('.pageloader').get_attribute('style'))=='display: block;'
            WebDriverWait(self.driver, 10).until(lambda b: b.find_element_by_css_selector('.pageloader').get_attribute('style'))=='display: none;'
            self.driver.find_element_by_css_selector('.hasPromoted>p')
            return print('Offers for {} were  found \n'.format(self.srch))
        except NoSuchElementException:
            return print('Offers for {} were not found \n'.format(self.srch))