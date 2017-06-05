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


class LoginPage(object):
    LOGIN_FIELD = (By.ID, 'userEmail')
    PASSWORD_FIELD = (By.ID, 'userPass')
    LOGIN_BUTTON = (By.ID, 'se_userLogin')
