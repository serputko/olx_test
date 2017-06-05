from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from pages.basepage import BasePage
from pages.locators import SearchPage as sp


class SearchPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.title = 'Крокодил - OLX.ua'

    def select_category(self, category):
        self.driver.find_element(*sp.COMBOBOX).click()
        self.list_of_categories = self.driver.find_elements(*sp.CATEGORY_DROPDOWN)
        self.items = [i.text for i in self.list_of_categories]
        for i, j in enumerate(self.items):
            if j.startswith(category):
                self.driver.find_element(*(sp.CERTAIN_CATEGORY[0], sp.CERTAIN_CATEGORY[1].format(i + 1))).click()

    def assert_results_consists(self, search):

        self.srch = search
        try:
            WebDriverWait(self.driver, 10).until(
                lambda b: b.find_element(*sp.LOADER).get_attribute('style')) == 'display: block;'
            WebDriverWait(self.driver, 10).until(
                lambda b: b.find_element(*sp.LOADER).get_attribute('style')) == 'display: none;'
            self.driver.find_element(*sp.SEARCH_RESULTS)
            return print('Offers for {} were  found \n'.format(self.srch))
        except NoSuchElementException:
            return print('Offers for {} were not found \n'.format(self.srch))
