Introduction
------------

This repository contains basic example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium).

Files
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pages/base.py](pages/base.py) contains PageObject pattern implementation for Python.

[pages/elements.py](pages/elements.py) contains helper class to define web elements on web pages.

[tests/test_smoke_yandex_market.py](tests/test_tmall_home_page.py) contains several smoke Web UI tests for YandexMarket (https://market.yandex.ru/)


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```

   ![alt text](example.png)
4 ) test_information:
	1. def test_auth_with_valid_data(web_browser):  # вход пользователя с валидными данными
    """Test_auth_with_valid_data"""
	2. def test_auth_with_invalid_data(web_browser):  # аутификация с неверными данными email password
    """Test_auth_with_invalid_data"""
	3. def test_negative_input_empty_string_email_and_password(web_browser):    # негативный тест ввод пустой строки в поле  ввода email and password
    """ Test negative input empty string email and password"""
	4. def test_negative_input_valid_email_field_with_valid_password(web_browser, fail_input_email_field):	# негативный тест ввод значений 'fail_input_email_field' в поле ввода email c валидным password
    """ Test negative input valid email with valid password"""
	5. def test_negative_input_password_field_with_valid_email(web_browser, fail_input_password_field):	#  негативный тест ввод значений 'fail_input_password_field' в поле ввода password c валидным email
    """ Test negative input password field with valid email"""
	6. def test_recovery_password_get_link(web_browser):	# тест переход на страницу восстановления пароля
    """Test get page recovery passsword"""
	7. def test_get_login_with_phone_number_link(web_browser):     # переход на страницу вход а по номеру телефона
    """Test get page login with phone number"""
	8. def test_get_instr_social_login(web_browser):    # тест переход на страницу инструкции входа через соц сети
    """ Test get instruction login with social auth"""
	9. def test_info_user_contract(web_browser):    # тест наличие информации о соглашении пользователя
    """ Test visible info user contract."""
	10. def test_get_link_login_with_ok_account(web_browser):    # тест переход на страницу входа соц сети одноклассники
    """Test get link login ok account."""
	11. def test_link_login_with_mailru_account(web_browser):   #  тест переход на страницу входа соц сети mail.ru
    """Test get login with mail.ru account."""
	12. def test_vizit_link_confidational(web_browser):     #  тест переход на страницу политика конфиденциальности
    """Test get link confidational"""
	13. def test_get_link_map(web_browser):     # тест переход на страницу карта сайта
    """ Test get map site"""
	14. def test_get_aliexpress(web_browser):  # переход на сайт "https://aliexpress.ru/"
    """Test get https://aliexpress.ru/"""
	15. def test_vizit_tmall_page(web_browser):    # тест проверка наличия элементов на странице tmall
    """vizit to tmall page."""
	16. def test_search_pozitive(web_browser, search_input):    # позитивный тест поиска по названию
    """ Make sure main search works fine. """
	17. def test_search_negative(web_browser, fail_input):  # негативный тест поиска по называнию fail_input
    """Test search negative."""
	18. def test_check_wrong_input_in_search(web_browser, wrong_input):  # тестовая проверка неправильного ввода в поиске
    """ Make sure that wrong keyboard layout input works fine. """
	19. def test_get_basket_shoping_card(web_browser):    # переход на страницу корзина покупок
    """Test get basket shoping card"""
	20. def test_vizit_favorite_page(web_browser):    # преход на страницу избранное
    """Test get favorite page"""
	21. def test_add_product_in_basket(web_browser):     # добавление товара в корзину
    """Test add product in basket""" 
	22. def test_check_sort_by_price(web_browser):    # тест проверка сортировки по цене
    """ Make sure that sort by price works fine."""
	23. def test_get_bayer_protection(web_browser):    # тест переход на страницу защита покупателя
    """Test get page bayer protection."""
	24. def test_get_support(web_browser):    # тест переход на страницу тех поддержки
    """Test get support"""
	25. def test_go_to_aliexpress(web_browser):     # тест переход на страницу  aliexpress
    """Test get to page aliexpress."""
	26. def test_get_online_chat(web_browser):     # тест переход на онлайн чат
    """Test get to online chat"""
	27. def test_get_warranty(web_browser):    # тест переход на страницу гарантии
    """Test get to warranty"""
	28. def test_count_language(web_browser):    # тест подсчет колличества языков после авторизации
    """Test count language."""
	29. def test_change_language_rus(web_browser):     # Тест выбор языка после авторизации - Сайт на русском.
    """Test change language rus."""
	30.  def test_change_language_bra(web_browser):    #  Тест выбор языка после авторизации - Site Brasil (Português)
    """Test change language Brasil (Português)."""
	31. def test_change_language_esp(web_browser):  # Тест выбор языка после авторизации - Sitio en español
    """Test change language español."""
	31. def test_change_language_fra(web_browser):  # Тест выбор языка после авторизации - Site France
    """Test change language France."""
	32. def test_change_language_pol(web_browser):  # Тест выбор языка после авторизации - Site Polskie
    """Test change language Polskie."""
	33. def test_change_language_tai(web_browser):    # Тест выбор языка после авторизации - Site Taiwan
    """Test change language Taiwan."""
	34. def test_change_language_turk(web_browser):    # Тест выбор языка после авторизации - Site Türkçe
    """Test change language Türkçe."""
	35. def test_change_language_deutesch(web_browser):     # Тест выбор языка после авторизации - Site Deutesch
    """Test change language Deutesch."""
	36. def test_change_language_korea(web_browser):    # Тест выбор языка после авторизации - Korea
    """Test change language Korea."""
	37. def test_get_myaliexpress(web_browser):    # Тест преход на страницу https://home.aliexpress.com/
    """Test get https://home.aliexpress.com/."""
	38. def test_vizit_myorder(web_browser):    # тест переход на страницу мои покупки
    """Test get my order"""
	39. def test_message_center_menu(web_browser):  # переход на страницу центр сообщений
    """Test get message center menu"""
	40. def test_my_wishes_menu(web_browser):    # тест переход на страницу мои желания
    """Test get my wishes"""
	41. def test_favorite_stores_menu(web_browser):    # тест переход на страницу любимые магазины
    """Test get favorite stores"""
	42. def test_my_coupons_menu(web_browser):  # тест переход на страницу мои купоны
    """Test get my coupons"""
	43. def test_get_report_copyright(web_browser):    # тест переход на страницу сообщить о нарущении авторских прав
    """Test get page Report Copyright Infringement"""
	44. def test_count_subcategory(web_browser):     # тест подсчет колличества подкатегорий
    """ Test count subcategory. """