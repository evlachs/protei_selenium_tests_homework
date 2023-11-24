from page_classes.base_page import BaseFoxPage
from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOCATOR_LOGIN_FIELD = (By.ID, 'loginEmail')
    LOCATOR_PASSWORD_FIELD = (By.ID, 'loginPassword')
    LOCATOR_AUTH_BUTTON = (By.ID, 'authButton')
    # вообще можно было бы использовать общий класс для почты и пароля, но по айдишникам же надежнее -_-
    LOCATOR_INVALID_EMAIL = (By.ID, 'emailFormatError')
    LOCATOR_INVALID_EMAIL_OR_PASSWORD = (By.ID, 'KEKEKEKEKEKKEKE')  # KEKEKEKEKEKKEKE, серьезно?:)
    LOCATOR_HELLO_MESSAGE = (By.CLASS_NAME, 'uk-legend')


class AuthPage(BaseFoxPage):
    def enter_login(self, login: str) -> None:
        login_field = self.find_element(AuthPageLocators.LOCATOR_LOGIN_FIELD)
        login_field.send_keys(login)

    def enter_password(self, password: str) -> None:
        login_field = self.find_element(AuthPageLocators.LOCATOR_PASSWORD_FIELD)
        login_field.send_keys(password)

    def click_auth_button(self) -> None:
        auth_button = self.find_element(AuthPageLocators.LOCATOR_AUTH_BUTTON)
        auth_button.click()

    def get_invalid_mail_check_error(self) -> str:
        text = self.find_element(AuthPageLocators.LOCATOR_INVALID_EMAIL).text
        return text

    def get_invalid_mail_or_password_error(self) -> str:
        text = self.find_element(AuthPageLocators.LOCATOR_INVALID_EMAIL_OR_PASSWORD).text
        return text
