from page_classes.table_page import TablePage
from page_classes.add_user_page import AddUserPage, AddUserPageLocators


def test_add_valid_user(driver):
    """
    Предусловие: пользователь авторизировался под тестовым аккаунтом и перешел на страницу добавления пользователя
    Действия теста: ввести валидные данные и попробовать добавить нового пользователя в таблицу;
    проверить наличие пользователя в таблице
    Ожидание: появится сообщение "Данные добавлены." и новый пользователь окажется в таблице
    """
    add_user_page = AddUserPage(driver)
    add_user_page.go_to_page('add_user')
    add_user_page.enter_email('sobaka@soma.com')
    add_user_page.enter_password('password')
    add_user_page.enter_name('SobakaSoma')
    add_user_page.select_gender('female')
    add_user_page.select_variants(1.2, '2.1', '2.3')
    add_user_page.find_element(AddUserPageLocators.LOCATOR_ADD_BUTTON).click()
    data_added_message = add_user_page.find_element(AddUserPageLocators.LOCATOR_DATA_ADDED).text
    assert data_added_message == 'Данные добавлены.', 'Не удалось добавить пользователя'
    add_user_page.find_element(AddUserPageLocators.LOCATOR_OK_BUTTON).click()

    table_page = TablePage(driver)
    table_page.go_to_page('users')
    data = table_page.get_table_data().split('\n')[-1]
    assert 'sobaka@soma.com SobakaSoma Женский 1.2 2.3' in data, 'Пользователь отстутствует в таблице'


def test_add_invalid_email_user(driver):
    """
    Предусловие: пользователь авторизировался под тестовым аккаунтом и перешел на страницу добавления пользователя
    Действия теста: ввести данные с невалидной почтой и попробовать добавить нового пользователя в таблицу;
    проверить, что пользователь не добавился в таблицу
    Ожидание: появится сообщение "Неверный формат E-Mail" и новый пользователь не добавится в таблицу
    """
    add_user_page = AddUserPage(driver)
    add_user_page.go_to_page('add_user')
    add_user_page.enter_email('new_user')
    add_user_page.enter_password('password')
    add_user_page.enter_name('Gangstas Paradise')
    add_user_page.select_gender('female')
    add_user_page.select_variants(1.2, '2.2', '2.1', '2.3')
    add_user_page.find_element(AddUserPageLocators.LOCATOR_ADD_BUTTON).click()
    invalid_data_message = add_user_page.find_element(AddUserPageLocators.LOCATOR_INVALID_DATA).text
    assert invalid_data_message == 'Неверный формат E-Mail', 'Удалось добавить пользователя'

    table_page = TablePage(driver)
    table_page.go_to_page('users')
    data = table_page.get_table_data()
    assert 'new_user Gangsta Paradise Женский 1.2 2.2, 2.3' not in data, 'Пользователь присутствует в таблице'


def test_add_invalid_password_user(driver):
    """
    Предусловие: пользователь авторизировался под тестовым аккаунтом и перешел на страницу добавления пользователя
    Действия теста: ввести данные с пустым паролем и попробовать добавить нового пользователя в таблицу;
    проверить, что пользователь не добавился в таблицу
    Ожидание: появится сообщение "Поле Пароль не может быть пустым" и новый пользователь не добавится в таблицу
    """
    add_user_page = AddUserPage(driver)
    add_user_page.go_to_page('add_user')
    add_user_page.enter_email('new_user@user.com')
    add_user_page.enter_password('')
    add_user_page.enter_name('Gangstas Paradise')
    add_user_page.select_gender('female')
    add_user_page.select_variants(1.2, '2.2', '2.1', '2.3')
    add_user_page.find_element(AddUserPageLocators.LOCATOR_ADD_BUTTON).click()
    invalid_data_message = add_user_page.find_element(AddUserPageLocators.LOCATOR_INVALID_DATA).text
    assert invalid_data_message == 'Поле Пароль не может быть пустым', 'Удалось добавить пользователя'

    table_page = TablePage(driver)
    table_page.go_to_page('users')
    data = table_page.get_table_data()
    assert 'new_user@user.com Gangsta Paradise Женский 1.2 2.2, 2.3' not in data, 'Пользователь присутствует в таблице'


def test_add_invalid_name_user(driver):
    """
    Предусловие: пользователь авторизировался под тестовым аккаунтом и перешел на страницу добавления пользователя
    Действия теста: ввести данные с пустым именем и попробовать добавить нового пользователя в таблицу;
    проверить, что пользователь не добавился в таблицу
    Ожидание: появится сообщение "Поле Имя не может быть пустым" и новый пользователь не добавится в таблицу
    """
    add_user_page = AddUserPage(driver)
    add_user_page.go_to_page('add_user')
    add_user_page.enter_email('new_user@user.com')
    add_user_page.enter_password('password')
    add_user_page.enter_name('')
    add_user_page.select_gender('female')
    add_user_page.select_variants(1.2, '2.2', '2.1', '2.3')
    add_user_page.find_element(AddUserPageLocators.LOCATOR_ADD_BUTTON).click()
    invalid_data_message = add_user_page.find_element(AddUserPageLocators.LOCATOR_INVALID_DATA).text
    assert invalid_data_message == 'Поле Имя не может быть пустым', 'Удалось добавить пользователя'

    table_page = TablePage(driver)
    table_page.go_to_page('users')
    data = table_page.get_table_data()
    assert 'new_user@user.com Женский 1.2 2.2, 2.3' not in data, 'Пользователь присутствует в таблице'
