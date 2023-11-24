from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class MenuNotFoundError(Exception):
    def __init__(self, message: str = 'На этой странице отсутствует меню.'):
        self.message = message

    def __str__(self):
        return self.message


class BasePageLocators:
    LOCATOR_NAVIGATION_MENU = (By.CLASS_NAME, 'uk-navbar-nav')
    LOCATOR_NAVIGATION_MENU_BUTTONS = (By.TAG_NAME, 'li')
    LOCATOR_MENU_AUTH_BUTTON = (By.ID, 'menuAuth')
    LOCATOR_MENU_MAIN_BUTTON = (By.ID, 'menuMain')
    LOCATOR_USERS_OPENER_BUTTON = (By.ID, 'menuUsersOpener')
    LOCATOR_USERS_BUTTON = (By.ID, 'menuUsers')
    LOCATOR_USER_ADD_BUTTON = (By.ID, 'menuUserAdd')
    LOCATOR_MORE_BUTTON = (By.ID, 'menuMore')


class BaseFoxPage:
    wait_time = 5

    def __init__(self, driver: webdriver.Chrome | webdriver.Firefox):
        self.driver = driver
        self.base_url = 'http://149.255.118.78:7080/'

    def find_element(self, locator) -> WebElement:
        return WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator) -> list[WebElement]:
        return WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_all_elements_located(locator))

    def go_to_page(self, page) -> None:
        self.driver.get(self.base_url+page)

    def get_navigation_menu_buttons(self) -> list[WebElement]:
        page_url = self.driver.current_url
        if 'auth' in page_url:
            raise MenuNotFoundError
        menu_buttons = self.find_elements(BasePageLocators.LOCATOR_NAVIGATION_MENU_BUTTONS)
        return menu_buttons
