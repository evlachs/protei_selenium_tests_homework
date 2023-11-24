from selenium.webdriver.common.by import By
from page_classes.base_page import BaseFoxPage


class MainPageLocators:
    LOCATOR_WELCOME_MESSAGE = (By.CLASS_NAME, 'uk-card-title')


class MainPage(BaseFoxPage):

    def get_welcome_message(self):
        message = self.find_element(MainPageLocators.LOCATOR_WELCOME_MESSAGE)
        return message.text
