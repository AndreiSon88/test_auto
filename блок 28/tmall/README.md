Introduction
------------


pattern with Selenium and Python (PyTest + Selenium).



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


4) test_information:




5) 1 test_auth_with_valid_data(web_browser):  # вход пользователя с валидными данными
    """Test_auth_with_valid_data"""


6) 2 test_auth_with_invalid_data(web_browser):  # аутификация с неверными данными email password
    """Test_auth_with_invalid_data"""
7) 3 test_negative_input_empty_string_email_and_password(web_browser):    # негативный тест ввод пустой строки в поле  ввода email and password
    """ Test negative input empty string email and password"""
8) 4 test_negative_input_valid_email_field_with_valid_password(web_browser, fail_input_email_field):	# негативный тест ввод значений 'fail_input_email_field' в поле ввода email c валидным password
    """ Test negative input valid email with valid password"""
9) 5 test_negative_input_password_field_with_valid_email(web_browser, fail_input_password_field):	#  негативный тест ввод значений 'fail_input_password_field' в поле ввода password c валидным email
    """ Test negative input password field with valid email"""
10) 6 test_recovery_password_get_link(web_browser):	# тест переход на страницу восстановления пароля
    """Test get page recovery passsword"""
11) 7 def test_get_login_with_phone_number_link(web_browser):     # переход на страницу вход а по номеру телефона
"""Test get page login with phone number"""
12) 8 def test_get_instr_social_login(web_browser):    # тест переход на страницу инструкции входа через соц сети
   """ Test get instruction login with social auth"""
13) 9 def test_info_user_contract(web_browser):    # тест наличие информации о соглашении пользователя
   """ Test visible info user contract."""
14) 10 def test_get_link_login_with_ok_account(web_browser):    # тест переход на страницу входа соц сети одноклассники
   """Test get link login ok account."""
15) 11 def test_link_login_with_mailru_account(web_browser):   #  тест переход на страницу входа соц сети mail.ru
   """Test get login with mail.ru account."""
16) 12 def test_vizit_link_confidational(web_browser):     #  тест переход на страницу политика конфиденциальности
   """Test get link confidational"""
17) 13 def test_get_link_map(web_browser):     # тест переход на страницу карта сайта
   """ Test get map site"""
18) 14 def test_get_aliexpress(web_browser):  # переход на сайт "https://aliexpress.ru/"
   """Test get https://aliexpress.ru/"""
19) 15 def test_vizit_tmall_page(web_browser):    # тест проверка наличия элементов на странице tmall
   """vizit to tmall page."""
20) 16 def test_search_pozitive(web_browser, search_input):    # позитивный тест поиска по названию
   """ Make sure main search works fine. """
21) 17 def test_search_negative(web_browser, fail_input):  # негативный тест поиска по называнию fail_input
   """Test search negative."""
22) 18 def test_check_wrong_input_in_search(web_browser, wrong_input):  # тестовая проверка неправильного ввода в поиске
   """ Make sure that wrong keyboard layout input works fine. """
23) 19 def test_get_basket_shoping_card(web_browser):    # переход на страницу корзина покупок
   """Test get basket shoping card"""
24) 20 def test_vizit_favorite_page(web_browser):    # преход на страницу избранное
   """Test get favorite page"""
25) 21 def test_add_product_in_basket(web_browser):     # добавление товара в корзину
   """Test add product in basket""" 
26) 22 def test_check_sort_by_price(web_browser):    # тест проверка сортировки по цене
   """ Make sure that sort by price works fine."""
27) 23 def test_get_bayer_protection(web_browser):    # тест переход на страницу защита покупателя
   """Test get page bayer protection."""
28) 24 def test_get_support(web_browser):    # тест переход на страницу тех поддержки
   """Test get support"""
29) 25 def test_go_to_aliexpress(web_browser):     # тест переход на страницу  aliexpress
   """Test get to page aliexpress."""
30) 26 def test_get_online_chat(web_browser):     # тест переход на онлайн чат
   """Test get to online chat"""
31) 27 def test_get_warranty(web_browser):    # тест переход на страницу гарантии
   """Test get to warranty"""
32) 28 def test_count_language(web_browser):    # тест подсчет колличества языков после авторизации
   """Test count language."""
33) 29 def test_change_language_rus(web_browser):     # Тест выбор языка после авторизации - Сайт на русском.
   """Test change language rus."""
34) 30 def test_change_language_bra(web_browser):    #  Тест выбор языка после авторизации - Site Brasil (Português)
   """Test change language Brasil (Português)."""
35) 31 def test_change_language_esp(web_browser):  # Тест выбор языка после авторизации - Sitio en español
   """Test change language español."""
36) 32 def test_change_language_fra(web_browser):  # Тест выбор языка после авторизации - Site France
   """Test change language France."""
37) 33 def test_change_language_pol(web_browser):  # Тест выбор языка после авторизации - Site Polskie
   """Test change language Polskie."""
38) 34 def test_change_language_tai(web_browser):    # Тест выбор языка после авторизации - Site Taiwan
   """Test change language Taiwan."""
39) 35 def test_change_language_turk(web_browser):    # Тест выбор языка после авторизации - Site Türkçe
   """Test change language Türkçe."""
40) 36 def test_change_language_deutesch(web_browser):     # Тест выбор языка после авторизации - Site Deutesch
   """Test change language Deutesch."""
41) 37 def test_change_language_korea(web_browser):    # Тест выбор языка после авторизации - Korea
   """Test change language Korea."""
42) 38 def test_get_myaliexpress(web_browser):    # Тест преход на страницу https://home.aliexpress.com/
   """Test get https://home.aliexpress.com/."""
43) 39 def test_vizit_myorder(web_browser):    # тест переход на страницу мои покупки
   """Test get my order"""
44) 40 def test_message_center_menu(web_browser):  # переход на страницу центр сообщений
   """Test get message center menu"""
45) 41 def test_my_wishes_menu(web_browser):    # тест переход на страницу мои желания
   """Test get my wishes"""
46) 42 def test_favorite_stores_menu(web_browser):    # тест переход на страницу любимые магазины
   """Test get favorite stores"""
47) 43 def test_my_coupons_menu(web_browser):  # тест переход на страницу мои купоны
   """Test get my coupons"""
48) 44 def test_get_report_copyright(web_browser):    # тест переход на страницу сообщить о нарущении авторских прав
   """Test get page Report Copyright Infringement"""
49) 45 def test_count_subcategory(web_browser):     # тест подсчет колличества подкатегорий
   """ Test count subcategory. """

