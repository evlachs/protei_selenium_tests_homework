from selenium.webdriver.common.by import By
from page_classes.base_page import BaseFoxPage


class TablePageLocators:
    LOCATOR_ADD_USER_BUTTON = (By.ID, 'addUser')
    LOCATOR_DATA_TABLE = (By.ID, 'dataTable')


class TablePage(BaseFoxPage):

    def get_table_data(self) -> str:
        data = self.find_element(TablePageLocators.LOCATOR_DATA_TABLE).text
        return data


