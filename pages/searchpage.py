
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
        return SearchPage(self)

    def assert_results_consists(self, search):
        self.srch = search
        try:
            self.driver.find_element(*sp.SEARCH_RESULTS)
            return print('Offers for {} were  found \n'.format(self.srch))
        except NoSuchElementException:
            return print('Offers for {} were not found \n'.format(self.srch))

    def select_district(self, district_name):
        self.driver.find_element(*sp.SELECT_DISTRICT_DROPDOWN).click()
        available_districts = self.driver.find_elements(*sp.DISTRICTS_LIST)
        for item in available_districts:
            if item.text == district_name:
                item.click()

    def input_from_price(self, price):
        self.driver.find_element(*sp.FROM_PRICE_FIELD).send_keys(price)

    def input_to_price(self, price):
        self.driver.find_element(*sp.TO_PRICE_FIELD).send_keys(price)

    def select_type_of_items(self, type):
        types_of_items = {
            'All': sp.ALL_ITEMS_LIST,
            'Private': sp.PRIVATE_ITEMS_LIST,
            'Business': sp.BUSINESS_ITEMS_LIST
        }
        try:
            type_selector = types_of_items[type]
            self.driver.find_element(*type_selector).click()
        except KeyError as e:
            raise ValueError('Undefined type of item: {}'.format(e.args[0]))

    def select_currency(self, currency):
        currency_types = {
            'HRN': sp.CURRENCY_HRYVNA,
            'USD': sp.CURRENCY_USD,
            'EUR': sp.CURRENCY_EURO
        }
        try:
            currency_selector = currency_types[currency]
            self.driver.find_element(*currency_selector).click()
        except KeyError as e:
            raise ValueError('Undefined currency: {}'.format(e.args[0]))

    def select_sorting_type(self, sort):
        sorting_types = {
            'New': sp.SORTING_NEW,
            'Cheap': sp.SORTING_CHEAPEST,
            'Expensive': sp.SORTING_MOST_EXPENSIVE
        }
        try:
            self.driver.implicitly_wait(3)
            sorting_selector = sorting_types[sort]
            self.driver.find_element(*sorting_selector).click()
        except KeyError as e:
            raise ValueError('Undefined sorting type: {}'.format(e.args[0]))
