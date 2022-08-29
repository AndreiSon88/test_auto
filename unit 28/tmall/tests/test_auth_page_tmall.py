import pytest
from pages.auth_page_tmall import TmallLoginPage
from config import generate_string, russian_chars, special_chars, chinese_chars, valid_email_tmall_page, \
    valid_password_tmall_page, invalid_email, invalid_password, link_cut


@pytest.mark.xfail(reason="появляется captcha")
def test_auth_with_valid_data(web_browser):  # вход пользователя с валидными данными
    """Test_auth_with_valid_data."""
    page = TmallLoginPage(web_browser)

    # page.login_btn.click()  # нажимаем кнопку Вход на странице login.aliexpress.ru
    # assert page.login_input_field.is_visible()  # проверяем что поле ввода login отображается на странице
    page.login_input_field.send_keys(valid_email_tmall_page)  # вводим валидный email
    # assert page.password_input_field.is_visible()  # проверяем что поле ввода password отображается на странице
    page.password_input_field.send_keys(valid_password_tmall_page)  # вводим валидный пароль
    page.enter_btn_login.click()  # нажимаем кнопку Войти на странице https://login.aliexpress.ru
    page.wait_page_loaded()  # ждем загрузки станицы
    page.sign_out_user_account_btn.is_visible()  # проверяем кнопка выйти видна на странице
    # cookie
    # pickle.dump(web_browser.get_cookies(), open("cookies","wb"))
    assert page.sign_in_user_account_btn.is_visible() == False  # проверяем кнопка войти на странице Tmall не видна
    assert page.sign_out_user_account_btn.is_visible()  # проверяем что видна кнопка Выйти
    page.sign_out_user_account_btn.click()  # нажимаем кнопку Выйти


@pytest.mark.xfail(reason="появляется captcha")
def test_auth_with_invalid_data(web_browser):  # аутификация с неверными данными email password
    """Test_auth_with_invalid_data."""
    page = TmallLoginPage(web_browser)
    assert "https://login.aliexpress.ru" in page.get_current_url()  # проверяем что перешли на страницу
    # login.aliexpress.ru
    page.login_btn.click()  # нажимаем кнопку Вход на странице login.aliexpress.ru
    assert page.login_input_field.is_visible()  # проверяем что поле ввода login отображается на странице
    page.login_input_field.send_keys(invalid_email)  # вводим невалидный email
    assert page.password_input_field.is_visible()  # проверяем что поле ввода password отображается на странице
    page.password_input_field.send_keys(invalid_password)  # вводим невалидный пароль
    page.enter_btn_login.click()  # нажимаем кнопку Войти на странице https://login.aliexpress.ru
    page.wait_page_loaded()
    assert page.incorrect_data_msg.is_visible()  # проверяем что появилось сообщение некорректные учетные данные


@pytest.mark.xfail(reason="появляется captcha")
def test_negative_input_empty_string_email_and_password(web_browser):    # негативный тест ввод пустой строки в поле
    # ввода email and password
    """ Test negative input empty string email and password."""
    page = TmallLoginPage(web_browser)
    # проверяем что перешли на страницу login.aliexpress.ru
    assert "https://login.aliexpress.ru" in page.get_current_url()
    page.wait_page_loaded()
    page.login_btn.click()  # нажимаем кнопку Вход на странице login.aliexpress.ru
    assert page.login_input_field.is_visible()  # проверяем что поле ввода login отображается на странице
    assert page.password_input_field.is_visible()  # проверяем что поле ввода password отображается на странице
    page.login_input_field.send_keys("")  # вводим в поле ввода login пустую строку
    page.password_input_field.send_keys("")  # вводим в поле ввода password пустую строку
    assert page.enter_btn_login.is_clickable() == False  # проверяем что кнопка Войти не кликабельна
    page.email_format_field_error_msg.is_presented()  # проверяем что появилось ссобщение об ошибке


@pytest.mark.parametrize('fail_input_email_field', ["dolim72899galotv.com",  # email без знака @
                                                    "@",  # знак @
                                                    "0",  # число 0
                                                    generate_string(255),  # строка 255 символов
                                                    generate_string(1001),  # строка 1001 символ
                                                    russian_chars(),  # русские символы
                                                    russian_chars().upper(),  # русские символы в верхнем регистре
                                                    special_chars(),  # спецсимволы
                                                    chinese_chars(),  # китайские символы
                                                    ])
@pytest.mark.xfail(reason="появляется captcha")
def test_negative_input_valid_email_field_with_valid_password(web_browser, fail_input_email_field):
    """ Test negative input valid email with valid password."""
    page = TmallLoginPage(web_browser)  # загружаем страницу "https://login.aliexpress.ru"
    # проверяем что перешли на страницу login.aliexpress.ru
    assert "https://login.aliexpress.ru" in page.get_current_url()
    page.wait_page_loaded()  # ждем загрузки страницы
    page.login_btn.click()  # нажимаем кнопку Вход на странице login.aliexpress.ru
    assert page.login_input_field.is_visible()  # проверяем что поле ввода login отображается на странице
    # вводим невалидное значения согласно списка 'fail_input_email_field'
    page.login_input_field.send_keys(fail_input_email_field)
    page.password_input_field.send_keys(valid_password_tmall_page)  # вводим в поле ввода password валидное значение
    page.enter_btn_login.click()  # нажимаем кнопку Войти
    page.email_format_field_error_msg.is_visible()  # проверяем что появилось сообщение об ошибке


@pytest.mark.parametrize('fail_input_password_field', ["*******",  # строка из символа "*"
                                                       "@",  # символ "@"
                                                       "0",  # символ "0"
                                                       generate_string(255),  # строка 255 символов
                                                       generate_string(1001),  # строка 1001 символов
                                                       russian_chars(),  # русские символы
                                                       russian_chars().upper(),  # русские символы в верхнем регистре
                                                       special_chars(),  # набор спецсимволов
                                                       chinese_chars(),  # китайские символы
                                                       ])
@pytest.mark.xfail(reason="появляется captcha")
# негативный тест ввод значений 'fail_input_email_field' в поле ввода password c валидным email
def test_negative_input_password_field_with_valid_email(web_browser, fail_input_password_field):
    """ Test negative input password field with valid email."""
    page = TmallLoginPage(web_browser)  # открываем страницу "https://login.aliexpress.ru"
    # проверяем что перешли на страницу login.aliexpress.ru
    assert "https://login.aliexpress.ru" in page.get_current_url()
    page.wait_page_loaded()  # ждем загрузки страницы
    page.login_btn.click()  # нажимаем кнопку Вход на странице login.aliexpress.ru
    assert page.login_input_field.is_visible()  # проверяем что поле ввода login отображается на странице
    page.login_input_field.send_keys(valid_email_tmall_page)  # вводим валидный email  в поле ввода email
    # вводим в поле ввода password  значения из списка fail_input_password_field
    page.password_input_field.send_keys(fail_input_password_field)
    page.enter_btn_login.click()  # нажимаем кнопку Войти
    assert page.password_format_field_error_msg.is_visible()  # проверяем что появилось ссобщение об ошибке


@pytest.mark.xfail(reason="появляется captcha")
def test_recovery_password_get_link(web_browser):   # тест переход на страницу восстановления пароля
    """Test get page recovery passsword."""
    page = TmallLoginPage(web_browser)  # загружаем страницу
    page.recovery_password_str_link.is_visible()  # проверяем что элемент виден на странице
    page.recovery_password_str_link.is_clickable()  # проверяем что элемент кликабелен
    href = page.recovery_password_str_link.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.recovery_password_str_link.click()  # нажимаем на элемент
    page.get(href)  # переходим по адрессу ссылки
    # проверяем что перешли на соответсвующую страницу
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


@pytest.mark.xfail(reason="появляется captcha")
def test_get_login_with_phone_number_link(web_browser):     # тест переход на страницу вход а по номеру телефона
    """Test get page login with phone number"""
    page = TmallLoginPage(web_browser)  # загружаем страницу
    # проверяем что элемент вход по телефону виден на странице
    assert page.login_with_phone_number_str_link.is_visible()   # проверяем что элемент вход по телефону кликабелен
    assert page.login_with_phone_number_str_link.is_clickable()  # проверяем что элемент вход по телефону кликабелен
    href = page.instr_social_login_btn.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.login_with_phone_number_str_link.click()  # нажимаем на элемент вход по телефону
    # проверяем что перешли на соответсвующую страницу
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"
    assert page.numbers_phone_input_field.is_visible()  # проверяем видимость поля ввода телефона


@pytest.mark.xfail(reason="появляется captcha")
def test_get_instr_social_login(web_browser):    # тест переход на страницу инструкции входа через соц сети
    """ Test get instruction login with social auth."""
    page = TmallLoginPage(web_browser)  # загружаем страницу
    page.wait_page_loaded()  # ждем загрузки страницы
    assert page.instr_social_login_btn.is_visible()  # проверяем что кнопка иструкция видна на странице
    assert page.instr_social_login_btn.is_clickable()  # проверяем что кнопка иструкция присутствует на странице
    href = page.instr_social_login_btn.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.instr_social_login_btn.click()  # нажимаем на кнопку
    page.get(href)  # переходим по ссылке
    # проверяем что перешли на соответсвующую страницу
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


@pytest.mark.xfail(reason="появляется captcha")
def test_info_user_contract(web_browser):    # тест наличие информации о соглашении пользователя
    """ Test visible info user contract."""
    page = TmallLoginPage(web_browser)  # загружаем страницу
    page.info_user_contract.scroll_to_element()  # скролим страницу до елемента
    if page.info_user_contract.is_visible():  # если элемент не виден
        page.info_user_contract.highlight_and_make_screenshot()  # делаем скришот


@pytest.mark.xfail(reason="появляется captcha")
def test_get_link_login_with_ok_account(web_browser):    # тест переход на страницу входа соц сети одноклассники
    """Test get link login ok account."""
    page = TmallLoginPage(web_browser)  # загружаем страницу
    assert page.ok_btn.is_visible  # проверяем что значок ok отображается
    assert page.ok_btn.is_clickable()  # проверяем что значок ok кликабельный
    page.ok_btn.scroll_to_element()  # скролим страницу до появления элемента
    page.ok_btn.click()  # нажимаем на значок ok
    href = page.vk_btn.get_attribute("href")  # сохраняем в переменную href адресс ссылки локатора
    # проверяем что перешли на страницу авторизации ok.ru
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


@pytest.mark.xfail(reason="появляется captcha")
def test_link_login_with_vk_account(web_browser):    # тест переход на страницу входа соц сети vk
    """Test get login with vk account"""
    page = TmallLoginPage(web_browser)  # загружаем страницу
    assert page.vk_btn.is_visible  # проверяем что значок vk отображается
    assert page.vk_btn.is_clickable()  # проверяем что значок vk кликабельный
    page.vk_btn.scroll_to_element()  # скролим страницу до появления элемента
    page.wait_page_loaded()  # ждем загрузки страницы
    href = page.vk_btn.get_attribute("href")  # сохраняем в переменную href адресс ссылки локатора
    page.vk_btn.click()  # нажимаем на значок vk
    # проверяем что перешли на страницу авторизации vk.ru
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


@pytest.mark.xfail(reason="появляется captcha")
def test_link_login_with_mailru_account(web_browser):   # тест переход на страницу входа соц сети mail.ru
    """Test get login with mail.ru account."""
    page = TmallLoginPage(web_browser)  # загружаем страницу
    assert page.mailru_btn.is_visible  # проверяем что значок mail.ru отображается
    assert page.mailru_btn.is_clickable()  # проверяем что значок mail.ru кликабельный
    page.mailru_btn.scroll_to_element()  # скролим страницу до появления элемента
    page.wait_page_loaded()  # ждем загрузки страницы
    href = page.mailru_btn.get_attribute("href")  # сохраняем в переменную href адресс ссылки локатора
    page.mailru_btn.click()  # нажимаем на значок mail.ru
    # проверяем что перешли на страницу авторизации mail.ru
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


def test_vizit_link_confidational(web_browser):     # тест переход на страницу политика конфиденциальности
    """Test get link confidational"""
    page = TmallLoginPage(web_browser)  # загружаем страницу
    page.scroll_down()  # спускаемся в низ страницы
    page.confidentional_link.scroll_to_element()  # скролим до елемента
    assert page.confidentional_link.is_visible()  # проверяем что элемент виден на странице
    assert page.confidentional_link.is_clickable()  # проверяем что элемент кликабельный
    href = page.confidentional_link.get_attribute("href")  # сохраняем в переменную href адресс ссылки локатора
    page.confidentional_link.click()  # нажимаем на элемент
    # проверяем что адресс ссылки ссответсвует текущей странице
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


def test_get_link_map(web_browser):     # тест переход на страницу карта сайта
    """ Test get map site"""
    page = TmallLoginPage(web_browser)  # загружаем страницу
    page.wait_page_loaded()  # ждем загрузки страницы
    page.scroll_down()  # спускаемся в низ страницы
    assert page.map_link.is_visible()  # проверяем что элемент виден на странице
    assert page.map_link.is_clickable()  # проверяем что элемент кликабельный
    href = page.map_link.get_attribute("href")  # сохраняем в переменную href адресс ссылки локатора
    page.map_link.click()  # нажимаем на элемент
    # проверяем что адресс ссылки ссответсвует текущей странице
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


@pytest.mark.xfail(reason="нестабильный тест ")
def test_get_aliexpress(web_browser):  # переход на сайт "https://aliexpress.ru/"
    """Test get https://aliexpress.ru/"""
    page = TmallLoginPage(web_browser)  # открываем страницу
    page.wait_page_loaded()  # ждем загрузки страницы
    assert page.logo_ali_on_login.is_visible()  # проверяем что логотип aliexpress виден
    href = page.logo_ali_on_login.get_attribute("href")  # сохраняем в переменную href адресс ссылки локатора
    page.logo_ali_on_login.click()  # нажимаем на логотип
    # проверяем что перешли на соответсвующую страницу
    assert link_cut(href) in page.get_current_url(), "страница не соответсвует ссылке"
