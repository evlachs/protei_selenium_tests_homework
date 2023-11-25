from page_classes.auth_page import AuthPage
from page_classes.main_page import MainPage


def test_valid_student_auth(driver):
    """
    Предусловие: пользователь находится на странице авторизации, у него валидные почта и пароль от аккаунта студента
    Действия теста: ввести валидную почту и валидный пароль от аккаунта студента, попробовать авторизироваться
    Ожидание: пользователь успешно авторизируется и увидит главную страницу с приветствием, а также возможность перейти
    на три страницы по меню в верхней части сайта: "Авторизация", "Главная страница", "Варианты".
    """
    auth_page = AuthPage(driver)
    main_page = MainPage(driver)
    auth_page.go_to_page('auth')
    auth_page.enter_login('student@protei.ru')
    auth_page.enter_password('student')
    auth_page.click_auth_button()
    result = main_page.get_welcome_message()
    assert result == 'Добро пожаловать!', 'Тест с данными студента провалился'
    menu_buttons = auth_page.get_navigation_menu_buttons()
    assert len(menu_buttons) == 3, 'Авторизация под студентом не прошла'


def test_valid_testing_account_auth(driver):
    """
    Предусловие: пользователь находится на странице авторизации, у него валидные почта и пароль от тестового аккаунта
    Действия теста: ввести валидную почту и валидный пароль от тестового аккаунта, попробовать авторизироваться
    Ожидание: пользователь успешно авторизируется и увидит главную страницу с приветствием, а также возможность перейти
    на пять страниц по меню в верхней части: "Авторизация", "Главная страница", "Варианты", и подменю кнопки
    "Пользователи" -> ["Таблица", "Добавление"]. Всего шесть гиперссылок.
    """
    auth_page = AuthPage(driver)
    main_page = MainPage(driver)
    auth_page.go_to_page('auth')
    auth_page.enter_login('test@protei.ru')
    auth_page.enter_password('test')
    auth_page.click_auth_button()
    result = main_page.get_welcome_message()
    assert result == 'Добро пожаловать!', 'Тест с данными от тестового аккаунта провалился'
    menu_buttons = auth_page.get_navigation_menu_buttons()
    assert len(menu_buttons) == 6, 'Авторизация под тестовым аккаунтом не прошла'


def test_invalid_mail_auth(driver):
    """
    Предусловие: пользователь находится на странице авторизации, у него невалидная почта
    Действия теста: ввести невалидную почту, попробовать авторизироваться
    Ожидание: пользователь не сможет войти в систему и увидит ошибку "Неверный формат E-Mail"
    """
    auth_page = AuthPage(driver)
    auth_page.go_to_page('auth')
    auth_page.enter_login('test@')
    auth_page.enter_password('test')
    auth_page.click_auth_button()
    result = auth_page.get_invalid_mail_check_error()
    assert result == 'Неверный формат E-Mail', 'Тест с неверным форматом почты провалился'


def test_invalid_mail_or_password_auth(driver):
    """
    Предусловие: пользователь находится на странице авторизации, у него валидная почта и невалдиный пароль
    Действия теста: ввести валидную почту и невалидный пароль, попробовать авторизироваться
    Ожидание: пользователь не сможет войти в систему и увидит ошибку "Неверный E-Mail или пароль"
    """
    auth_page = AuthPage(driver)
    auth_page.go_to_page('auth')
    auth_page.enter_login('test@protei.ru')
    auth_page.enter_password('123')
    auth_page.click_auth_button()
    result = auth_page.get_invalid_mail_or_password_error()
    assert result == 'Неверный E-Mail или пароль', 'Тест с неверным паролем провалился'
