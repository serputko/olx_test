class BasePage(object):
    def __init__(self, context):
        self.driver = context.driver
        self.title = ''
        self.url = ''

    def open(self):
        self.driver.get(self.url)
        return self

    def get_title(self):
        return self.driver.title

    def is_displayed(self):
        return self.get_title() == self.title
