from page_classes.base_page import BaseFoxPage
from selenium.webdriver.common.by import By


class GenderError(Exception):  # актуалочка
    def __init__(self, message: str = 'Ошибка выбора пола, укажите пол "male" или "female"'):
        self.message = message

    def __str__(self):
        return self.message


class VariantError(Exception):
    def __init__(self, message: str = 'Ошибка выбора варианта; укажите один вариант из списка: 1.1, 1.2 и '
                                      'любое количество вариантов из списка: 2.1, 2.2, 2.3'):
        self.message = message

    def __str__(self):
        return self.message


class AddUserPageLocators:
    LOCATOR_ADD_USER_INSCRIPTION = (By.CLASS_NAME, 'uk-legend')
    LOCATOR_EMAIL_FIELD = (By.ID, 'dataEmail')
    LOCATOR_PASSWORD_FIELD = (By.ID, 'dataPassword')
    LOCATOR_NAME_FIELD = (By.ID, 'dataName')
    LOCATOR_GENDER_FIELD = (By.ID, 'dataGender')
    LOCATOR_GENDER_OPTIONS = (By.TAG_NAME, 'option')
    LOCATOR_ADD_BUTTON = (By.ID, 'dataSend')
    LOCATOR_DATA_ADDED = (By.CLASS_NAME, 'uk-modal-body')
    LOCATOR_OK_BUTTON = (By.CLASS_NAME, 'uk-modal-close')
    # в этот раз все же попробую по общему классу для сообщений о невалидных данных
    LOCATOR_INVALID_DATA = (By.CLASS_NAME, 'uk-alert')
    LOCATOR_VARIANTS_DICT = {
        '1.1': (By.ID, 'dataSelect11'),
        '1.2': (By.ID, 'dataSelect12'),
        '2.1': (By.ID, 'dataSelect21'),
        '2.2': (By.ID, 'dataSelect22'),
        '2.3': (By.ID, 'dataSelect23')
    }


class AddUserPage(BaseFoxPage):

    def enter_email(self, email: str = None) -> None:
        email_field = self.find_element(AddUserPageLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_password(self, password: str = None) -> None:
        password_field = self.find_element(AddUserPageLocators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password)

    def enter_name(self, name: str = None) -> None:
        name_field = self.find_element(AddUserPageLocators.LOCATOR_NAME_FIELD)
        name_field.send_keys(name)

    def select_gender(self, gender: str = 'male') -> None:
        """
        :param gender: Параметр выбора пола пользователся выбирать из вариантов "male" или "female" (default='male')
        :type gender: str

        :raises GenderError: Ошибка выбора пола; возникает при переданном значении, отличном от "male" или "female"
        """
        self.find_element(AddUserPageLocators.LOCATOR_GENDER_FIELD).click()
        gender_options = self.find_elements(AddUserPageLocators.LOCATOR_GENDER_OPTIONS)
        if gender.lower() == 'male':
            gender_options[0].click()
        elif gender.lower() == 'female':
            gender_options[1].click()
        else:
            raise GenderError

    def select_variants(self, *args: str | float) -> None:
        """
        :param args: Выбранные варианты для пользователя: 1.1 или 1.2 (один из двух), 2.1, 2.2, 2.3 (любая комбинация);
        при передаче двух вариантов 1.1 и 1.2 будет выбран последний переданный в функцию вариант
        :type args: str | float

        :raises VariantError: Ошибка, возникающая при передаче в функцию несуществующего варианта
        """
        if not args:
            raise VariantError
        variants = [str(var) for var in args]
        for variant in variants:
            if variant not in AddUserPageLocators.LOCATOR_VARIANTS_DICT.keys():
                raise VariantError
            self.find_element(AddUserPageLocators.LOCATOR_VARIANTS_DICT[variant]).click()
