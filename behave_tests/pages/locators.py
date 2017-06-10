from selenium.webdriver.common.by import By


class HomePage(object):
    INPUT_FIELD = (By.CSS_SELECTOR, 'input.queryfield')
    SEARCH_BUTTON = (By.ID, 'submit-searchmain')
    PROFILE_BUTTON = (By.ID, 'topLoginLink')


class SearchPage(object):
    CERTAIN_CATEGORY = (By.CSS_SELECTOR, '#categorySelectList>li:nth-child({})')
    COMBOBOX = (By.CSS_SELECTOR, 'div.combospace')
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, '#categorySelectList>li>a')
    LOADER = (By.CSS_SELECTOR, '.pageloader')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.hasPromoted>p')
    SELECT_DISTRICT_DROPDOWN = (By.CLASS_NAME, 'district')
    DISTRICTS_LIST = (By.CLASS_NAME, '.districts li a')
    FROM_PRICE_FIELD = (By.CLASS_NAME, 'filter-item-from')
    TO_PRICE_FIELD = (By.CLASS_NAME, 'filter-item-to')
    ALL_ITEMS_LIST = (By.CSS_SELECTOR, '.view-lists+ul.sort-order-type li:nth-child(1)')
    PRIVATE_ITEMS_LIST = (By.CSS_SELECTOR, '.view-lists+ul.sort-order-type li:nth-child(2)')
    BUSINESS_ITEMS_LIST = (By.CSS_SELECTOR, '.view-lists+ul.sort-order-type li:nth-child(3)')
    CURRENCY_HRYVNA = (By.CSS_SELECTOR, '.view-currency.currencySelector li:nth-child(2)')
    CURRENCY_USD = (By.CSS_SELECTOR, '.view-currency.currencySelector li:nth-child(3)')
    CURRENCY_EURO = (By.CSS_SELECTOR, '.view-currency.currencySelector li:nth-child(4)')
    SORTING_NEW = (By.CSS_SELECTOR, '.view-lists ul.sort-order-type li:nth-child(2) a')
    SORTING_CHEAPEST = (By.CSS_SELECTOR, '.view-lists ul.sort-order-type li:nth-child(2) a')
    SORTING_MOST_EXPENSIVE = (By.CSS_SELECTOR, '.view-lists ul.sort-order-type li:nth-child(2) a')


class LoginPage(object):
    LOGIN_FIELD = (By.ID, 'userEmail')
    PASSWORD_FIELD = (By.ID, 'userPass')
    LOGIN_BUTTON = (By.ID, 'se_userLogin')
    WRONG_PASSWORD_ERROR_MESSAGE = (By.CSS_SELECTOR, '.errorboxContainer [for=userPass]')
