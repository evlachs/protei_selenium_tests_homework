from page_classes.auth_page import AuthPageLocators
from page_classes.main_page import MainPageLocators
from page_classes.table_page import TablePageLocators
from page_classes.add_user_page import AddUserPageLocators
from page_classes.variants_page import VariantsUserPageLocators
from page_classes.base_page import BaseFoxPage, BasePageLocators


def test_navigation_menu(driver):
    """
    Предусловие: пользователь авторизовался под тестовым аккаунтом и находится на главной странице
    Действия теста: переход по всем доступным гиперссылкам в меню верхней части страницы
    Ожидание: удастся последовательно перейти на все доступные страницы по гиперссылкам меню
    """
    page = BaseFoxPage(driver)
    page.go_to_page('main')
    page.find_element(BasePageLocators.LOCATOR_USERS_OPENER_BUTTON).click()
    page.find_element(BasePageLocators.LOCATOR_USERS_BUTTON).click()
    add_user_button = page.find_element(TablePageLocators.LOCATOR_ADD_USER_BUTTON).text
    assert add_user_button == 'ДОБАВИТЬ ПОЛЬЗОВАТЕЛЯ', 'Переход на страницу с таблицей не удался'
    page.find_element(BasePageLocators.LOCATOR_USERS_OPENER_BUTTON).click()
    page.find_element(BasePageLocators.LOCATOR_USER_ADD_BUTTON).click()
    add_user_inscription = page.find_element(AddUserPageLocators.LOCATOR_ADD_USER_INSCRIPTION).text
    assert add_user_inscription == 'Добавление пользователя', 'Переход на страницу добавления пользователей не удался'
    page.find_element(BasePageLocators.LOCATOR_MORE_BUTTON).click()
    page.find_element(VariantsUserPageLocators.LOCATOR_LOGO)
    protei_inscription = page.find_element(VariantsUserPageLocators.LOCATOR_NCT_PROTEI).text
    assert protei_inscription == 'НТЦ ПРОТЕЙ', 'Переход на страницу "Варианты" не удался'
    page.find_element(BasePageLocators.LOCATOR_MENU_MAIN_BUTTON).click()
    welcome_message = page.find_element(MainPageLocators.LOCATOR_WELCOME_MESSAGE).text
    assert welcome_message == 'Добро пожаловать!', 'Переход на главную страницу не удался'
    page.find_element(BasePageLocators.LOCATOR_MENU_AUTH_BUTTON).click()
    hello_message = page.find_element(AuthPageLocators.LOCATOR_HELLO_MESSAGE).text
    assert hello_message == 'Привет с демо-сайта для автотестов!', 'Переход на страницу авторизации не удался'
