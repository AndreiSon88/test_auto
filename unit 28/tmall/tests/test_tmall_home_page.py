# !/usr/bin/python3 -*- encoding=utf8 -*- How to run: 1) Download geko driver for Chrome here:
# https://chromedriver.chromium.org/downloads 2) Install all requirements: pip install -r requirements.txt 3) Run
# tests: python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/* python -m pytest -v --driver Chrome
# --driver-path C:\chromedriver_win32\chromedriver.exe -s -k "_negative_input_valid_email_field_with_valid_password"
import pytest

from pages.tmall_home_page import TmallPage

from config import generate_string, special_chars, chinese_chars, valid_email_tmall_page, valid_password_tmall_page, \
    url_base, language, link_cut
import time


def test_vizit_tmall_page(web_browser):  # тест проверка наличия элементов на странице tmall
    """vizit to tmall page."""
    page = TmallPage(web_browser)  # загрузка страницы и уатификация
    assert page.logo_tmall.is_visible()  # проверка наличие логотипа tmall
    assert page.gif_logo_tmall.is_visible()  # проверка наличие логотипа tmall анимация
    assert page.search.is_visible()  # проверка наличие поле поиска
    assert page.search_run_button.is_visible()  # проверка наличие кнопки поиска
    assert page.logo_ali.is_visible()  # проверка наличие логотипа aliexpress


@pytest.mark.parametrize('search_input', ["iphone 12",
                                          "смартфон",
                                          "ключ",
                                          "usb"])
@pytest.mark.xfail(reason="Не стабильная работа поиска")
def test_search_pozitive(web_browser, search_input):  # позитивный тест поиска по названию
    """ Make sure main search works fine. """

    page = TmallPage(web_browser)  # загрузка страницы и уатификация
    page.search.send_keys(f'{search_input}')  # вводим в поле ввода значение search_input
    page.search_run_button.click()  # нажимаем на кнопку поиск

    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0  # проверка результата поиска

    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{search_input}' in title.lower(), msg  # проверка что  search_input встречается в описании товара


@pytest.mark.parametrize('fail_input', ["",  # пустая строка
                                        "0",  # ноль
                                        generate_string(255),  # строка 255 символов
                                        generate_string(1001),  # строка 1001 символ
                                        special_chars(),  # строка спецсимволов
                                        chinese_chars()])  # китайские символы
@pytest.mark.xfail(reason="Не стабильная работа поиска")
def test_search_negative(web_browser, fail_input):  # негативный тест поиска по называнию fail_input
    """Test search negative."""
    page = TmallPage(web_browser)  # загрузка страницы и аутификация через cookie
    page.search.send_keys(f'{fail_input}')  # вводим в поле ввода значение search_input
    page.search_run_button.click()  # нажимаем на кнопку поиск
    assert page.search_error.is_visible()  # проверка ошибка поиска видна на странице

    # Make sure user found the relevant products
    # for title in page.products_titles.get_text():
    #     msg = 'Wrong product in search "{}"'.format(title)
    #     assert 'iphone' in title.lower(), msg


@pytest.mark.parametrize("wrong_input", ['cvfhnajy', 'kjgfnf', 'ks;b'], ids=["смартфон", "лопата", "лыжи"])
@pytest.mark.xfail(reason="Не стабильная работа поиска")
def test_check_wrong_input_in_search(web_browser, wrong_input):  # тестовая проверка неправильного ввода в поиске
    """ Make sure that wrong keyboard layout input works fine. """

    page = TmallPage(web_browser)  # загрузка страницы и аутификация через cookie

    # Try to enter "wrong_input" with English keyboard:
    page.search = wrong_input
    page.search_run_button.click()  # нажимаем на кнопку поиска

    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0  # проверяем что присутсвуют товары

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'смартфон' or "лопата" or "лыжи" in title.lower(), msg


def test_get_basket_shoping_card(web_browser):  # переход на страницу корзина покупок
    """Test get basket shoping card"""
    page = TmallPage(web_browser)  # загрузка страницы и аутификация через cookie
    page.wait_page_loaded()  # ждем загрузки страницы
    page.basket_icon_shoping_card.is_visible()  # проверяем видимость иконки корзины
    page.basket_icon_shoping_card.click()  # кликаем на иконку корзины
    # проверяем что href соответствует странице
    assert 'https://www.aliexpress.com/p/shoppingcart/index.html' in page.get_current_url()
    page.wait_page_loaded()  # ждем загрузки страницы
    page.icon_basket.click()
    assert page.msg_basket_empty.is_visible(), 'отсутсвует сообщение корзина пуста'


@pytest.mark.xfail(reason="при авторизации через cookie переходит на https://login.aliexpress.com/")
def test_vizit_favorite_page(web_browser):  # преход на страницу избранное
    """Test get favorite page"""
    page = TmallPage(web_browser)  # загрузка страницы и аутификация через cookie
    href = page.favorite_icon.get_attribute("href")  # выделяем ссылку из элемента
    page.favorite_icon.click()  # наимаем на элемент
    assert link_cut(href) in page.get_current_url()


@pytest.mark.xfail(reason="при авторизации через cookie не появляется товар в корзине")
def test_add_product_in_basket(web_browser):  # добавление товара в корзину
    """Test add product in basket"""
    page = TmallPage(web_browser)  # загрузка страницы и аутификация через cookie
    page.search.send_keys("Ключ динамометрический DEKO DKTW01 1/4 5-25 Нм")
    page.search_run_button.click()  # нажимаем на кнопку поиска
    page.product_wrench.wait_to_be_clickable()  # ждем пока элемент станет кликабельным
    page.product_wrench.click()  # нажимаем на элемент
    href_product = page.product_wrench.get_attribute("href")  # выделяем ссылку из элемента
    page.get(href_product)  # переходим по ссылке
    assert page.product_name.is_visible(), 'не отображается  название продукта'
    assert page.product_price.is_visible(), 'не отображается цена продукта '
    page.btn_in_basket.click()  # нажимаем на иконку корзины
    assert page.btn_in_basket.is_visible(), 'не отображается кнопка добавить в корзину'

    page.get(url_base)  # переходим на страницу Tmall
    page.basket_icon_shoping_card.click()  # нажимаем на иконку корзины
    page.icon_basket.click()
    # проверяем надичие товара в корзине
    assert page.list_product_in_basket.is_visible(), "list_product_in_basket.is_not_visible()"


@pytest.mark.parametrize("input_test_price", ['чайник', 'телефон', 'book', 'camera'])
@pytest.mark.xfail(reason="Filter by price doesn't work")
def test_check_sort_by_price(web_browser, input_test_price):  # тест проверка сортировки по цене
    """ Make sure that sort by price works fine."""

    page = TmallPage(web_browser)  #

    page.search = input_test_price  # вводим в поле поиска значение
    page.search_run_button.click()  # нажимаем кнопку поиск

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_price_btn.scroll_to_element()  # скролим до элемнта сортировка по цене
    page.sort_price_btn.click()  # нажимаем на элемент сортировка по цене
    page.wait_page_loaded()  # ждем загрузки страницы
    time.sleep(2)

    # Get prices of the products in Search results
    all_prices = page.sort_price_result.get_text()
    all_prices.remove('')
    print(all_prices)

    # Convert all prices from strings to numbers
    all_prices1 = []

    for p in all_prices:
        p = p.replace(' руб.', '')
        p = p.replace(' ', '')
        p = p.replace(',', '.')
        if p == '':
            break
        p = float(p)
        all_prices1.append(p)

    print(all_prices1)
    print(sorted(all_prices1))

    # Make sure products are sorted by price correctly:
    assert all_prices1 == sorted(all_prices1), "Sort by price doesn't work!"


def test_get_bayer_protection(web_browser):  # тест переход на страницу защита покупателя
    """Test get page bayer protection."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизуемся
    assert page.bayer_protection.is_visible()  # проверяем наличие элемента защита покупателя
    page.bayer_protection.click()  # нажимаем на елемент защита покупателя
    # проверяем переход на соответствующую страницу "https://www.aliexpress.com/p/buyerprotection/index.html"
    assert "https://www.aliexpress.com/p/buyerprotection/index.html" in page.get_current_url()
    for info in page.info_bayer_protection.get_text():
        assert len(info) > 0, f"not found info bayer protection"  # проверяем наличие текста на странице защита
        # пользователя


def test_get_support(web_browser):  # тест переход на страницу тех поддержки
    """Test get support"""
    page = TmallPage(web_browser)  # загружаем страницу и авторизуемся через cookie
    page.menu_help.click()  # нажимаем на выпадающее меню помощь
    page.support.click()  # нажимаем на элемент техподдержка
    # проверяем что перешли на соответсвующую страницу
    assert 'https://customerservice.aliexpress.com/home' in page.get_current_url(), "текущая страница соответсвует " \
                                                                                    "ссылке "
    assert page.logo_help_centr.is_visible()  # проверяем что виден логотип центра помощи


def test_go_to_aliexpress(web_browser):  # тест переход на страницу  aliexpress
    """Test get to page aliexpress."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизуемся через cookie
    assert page.logo_ali.is_visible()  # проверяем что логотип виден на странице
    assert page.logo_ali.is_presented()  # проверяем что логотип присутствует на странице
    href = page.logo_ali.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.logo_ali.click()  # нажимаем на логотип
    # проверяем что перешли на соответсвующую страницу
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


def test_get_online_chat(web_browser):  # тест переход на онлайн чат
    """Test get to online chat"""
    page = TmallPage(web_browser)  # загружаем страницу и авторизуемся через cookie
    assert page.online_chat.is_visible()  # проверяем видимость элемента онлайн чат
    href = page.online_chat.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.online_chat.click()  # нажимаем на элемент онлайн чат
    # page.background_login.delete()  # удаляем всплывающее сообщение
    # проверяем что перешли на соответсвующую страницу
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_get_warranty(web_browser):  # тест переход на страницу гарантии
    """Test get to warranty"""
    page = TmallPage(web_browser)  # загружаем страницу и авторизуемся через cookie
    assert page.warranty.is_visible()  # проверяем что элемент гарантии виден на странице
    page.refresh()  # обновляем страницу
    href = page.warranty.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.warranty.click()  # нажимаем на элемент гарантии
    # проверяем что перешли на соответсвующую страницу
    assert link_cut(href) in page.get_current_url(), f"текущая страница не соответсвует ссылке{href}"


def test_count_language(web_browser):  # тест подсчет колличества языков после авторизации
    """Test count language."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    time.sleep(3)
    page.language.click()  # нажимаем на значок язык
    # проверяем наличие языка в списке language
    for i in page.contain_language.get_text():
        assert i in language, f"{i}language not found"


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_rus(web_browser):  # Тест выбор языка после авторизации - Сайт на русском.
    """Test change language rus."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.rus.click()  # нажимаем елемент сайт на русском
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    page.menu_city_language.click()  # выпадающее меню выбор языка страницы
    assert page.rus_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_bra(web_browser):  # Тест выбор языка после авторизации - Site Brasil (Português)
    """Test change language Brasil (Português)."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.bra.click()  # нажимаем елемент сайт на Português
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    page.menu_city_language.click()  # выпадающее меню выбор языка страницы
    assert page.bra_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_esp(web_browser):  # Тест выбор языка после авторизации - Sitio en español
    """Test change language español."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.esp.click()  # нажимаем елемент сайт на español
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    page.menu_city_language.click()  # нажимаем на выпадающее меню выбор языка страницы
    assert page.esp_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_fra(web_browser):  # Тест выбор языка после авторизации - Site France
    """Test change language France."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.fra.click()  # нажимаем елемент сайт на France
    time.sleep(2)
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    if page.fra_coupon.is_visible():  # если появляется купон
        page.background_coopon.delete()  # удаляем задний фон купона
    page.menu_city_language.click()  # нажимаем на выпадающее меню выбор языка страницы
    assert page.fra_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_pol(web_browser):  # Тест выбор языка после авторизации - Site Polskie
    """Test change language Polskie."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.pol.click()  # нажимаем елемент сайт на Polskie
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    if page.background_coopon.is_visible():  # если появляется купон
        page.background_coopon.delete()  # удаляем задний фон купона
    page.menu_city_language.click()  # нажимаем на выпадающее меню выбор языка страницы
    assert page.pol_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_tai(web_browser):  # Тест выбор языка после авторизации - Site Taiwan
    """Test change language Taiwan."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.tai.click()  # нажимаем елемент сайт на Taiwan
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    if page.background_coopon.is_visible():  # если появляется купон
        page.background_coopon.delete()  # удаляем задний фон купона
    page.menu_city_language.click()  # нажимаем на выпадающее меню выбор языка страницы
    assert page.tai_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_itl(web_browser):  # Тест выбор языка после авторизации - Site italia (Italiano)
    """Test change language italia (Italiano)."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.itl.click()  # нажимаем елемент сайт на italia
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    if page.background_coopon.is_visible():  # если появляется купон
        page.background_coopon.delete()  # удаляем задний фон купона
    page.menu_city_language.click()  # нажимаем на выпадающее меню выбор языка страницы
    assert page.itl_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_turk(web_browser):  # Тест выбор языка после авторизации -  Türkçe
    """Test change language Türkçe."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.turk.click()  # нажимаем елемент сайт на Türkçe
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    if page.background_coopon.is_visible():  # если появляется купон
        page.background_coopon.delete()  # удаляем задний фон купона
    page.menu_city_language.click()  # нажимаем на выпадающее меню выбор языка страницы
    assert page.turk_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_deutesch(web_browser):  # Тест выбор языка после авторизации -  Deutesch
    """Test change language Deutesch."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.deutesch.click()  # нажимаем елемент сайт на Deutesch
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    if page.background_coopon.is_visible():  # если появляется купон
        page.background_coopon.delete()  # удаляем задний фон купона
    page.menu_city_language.click()  # нажимаем на выпадающее меню выбор языка страницы
    assert page.deutesch_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_korea(web_browser):  # Тест выбор языка после авторизации - Korea
    """Test change language Korea."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.korea.click()  # нажимаем елемент сайт на Korea
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    if page.background_coopon.is_visible():  # если появляется купон
        page.background_coopon.delete()  # удаляем задний фон купона
    page.menu_city_language.click()  # нажимаем на выпадающее меню выбор языка страницы
    assert page.korea_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="нестабильный тест переходит на страницу 'https://aliexpress.ru/' ")
def test_change_language_arabian(web_browser):  # Тест выбор языка после авторизации - Arabian
    """Test change language Arabian."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookie
    page.language.click()  # нажимаем на вкладку язык
    page.arabian.click()  # нажимаем елемент сайт на Arabian
    assert "aliexpress.ru/" in page.get_current_url()  # проверяем что перешли на страницу aliexpress.ru/
    if page.background_coopon.is_visible():  # если появляется купон
        page.background_coopon.delete()  # удаляем задний фон купона
    page.menu_city_language.click()  # нажимаем на выпадающее меню выбор языка страницы
    assert page.arabian_msg.is_visible()  # проверяем видимость языка в открывшемся меню


@pytest.mark.xfail(reason="502 Bad Gateway")
def test_get_myaliexpress(web_browser):  # Тест преход на страницу https://home.aliexpress.com/
    """Test get https://home.aliexpress.com/."""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookiе
    page.user_account_info_icon.click()  # нажимаем на вкладку язык
    href = page.message_center_menu.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.my_aliexpress_link.click()  # нажимаем на элемент мой алиэкспресс
    # проверяем что перешли на соответсвующую страницу
    assert link_cut(href) in page.get_current_url(), "страница не соответсвует ссылке"
    assert page.logo_ali.is_presented()  # проверяем что присутсвет логотип aliexpress


@pytest.mark.xfail(reason="ошибка авторизации на странице https://www.aliexpress.com/ при авторизации через cookie ")
def test_vizit_myorder(web_browser):  # тест переход на страницу мои покупки
    """Test get my order"""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookiе
    page.user_account_info_icon.click()  # нажимаем на иконку пользователя
    href = page.my_order_menu.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.my_order_menu.click()  # нажимаем на элемент мои заказы
    # проверяем что перешли на соответсвующую страницу
    if link_cut(href) in page.get_current_url():  # если появлется страница авторизации вводим валидные логин и пароль
        page.fm_login_id.send_keys(valid_email_tmall_page)
        page.fm_login_password.send_keys(valid_password_tmall_page)
        page.btn_in_login.click()
    assert link_cut(href) in page.get_current_url(), "страница не соответсвует ссылке"
    assert page.logo_ali.is_visible()  # проверяем что присутсвет логотип aliexpress


@pytest.mark.xfail(reason="переход на страницу https://login.aliexpress.com/")
def test_message_center_menu(web_browser):  # переход на страницу центр сообщений
    """Test get message center menu"""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookiе
    page.user_account_info_icon.click()  # нажимаем на иконку пользователя
    href = page.message_center_menu.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.message_center_menu.click()  # нажимаем на элемент центр сообщений
    assert link_cut(href) in page.get_current_url(), "страница не соответсвует ссылке"
    assert page.logo_ali.is_visible()  # проверяем что присутсвет логотип aliexpress


@pytest.mark.xfail(reason="переход на страницу https://login.aliexpress.com/")
def test_my_wishes_menu(web_browser):  # тест переход на страницу мои желания
    """Test get my wishes"""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookiе
    page.user_account_info_icon.click()  # нажимаем на иконку пользователя
    href = page.my_wishes_menu.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.my_wishes_menu.click()  # нажимаем на элемент мои желания
    assert link_cut(href) in page.get_current_url(), "страница не соответсвует ссылке"
    assert page.logo_ali.is_visible()  # проверяем что присутсвет логотип aliexpress


@pytest.mark.xfail(reason="переход на страницу https://login.aliexpress.com/")
def test_favorite_stores_menu(web_browser):  # тест переход на страницу любимые магазины
    """Test get favorite stores"""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookiе
    page.user_account_info_icon.click()  # нажимаем на иконку пользователя
    href = page.favorite_stores_menu.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.favorite_stores_menu.click()  # нажимаем на элемент любимые магазины

    assert link_cut(href) in page.get_current_url(), "страница не соответсвует ссылке"
    assert page.logo_ali.is_visible()  # проверяем что присутсвет логотип aliexpress


@pytest.mark.xfail(reason="переход на страницу https://login.aliexpress.com/")
def test_my_coupons_menu(web_browser):  # тест переход на страницу мои купоны
    """Test get my coupons"""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookiе
    page.user_account_info_icon.click()  # нажимаем на иконку пользователя
    href = page.my_coupons_menu.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.my_coupons_menu.click()  # нажимаем на элемент мои купоны

    assert link_cut(href) in page.get_current_url(), "страница не соответсвует ссылке"
    assert page.logo_ali.is_visible()  # проверяем что присутсвет логотип aliexpress


def test_get_report_copyright(web_browser):  # тест переход на страницу сообщить о нарущении авторских прав
    """Test get page Report Copyright Infringement"""
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookiе
    page.wait_page_loaded()  # ждем загрузки страницы
    page.report_copyright.scroll_to_element()  # скролим до элемента  Сообщить о нарушении авторских прав
    time.sleep(15)
    assert page.report_copyright.wait_to_be_clickable()  # ждем пока элемент будет кликабельный
    href = page.report_copyright.get_attribute("href")  # выделяем ссылку и сохраняем в переменную href
    page.scroll_down()  # скролим страницу вниз
    page.scroll_down()

    page.report_copyright.wait_to_be_clickable(50)  # ждем пока элемент будет кликабельный
    page.report_copyright.click()  # нажимаем на элемент
    page.wait_page_loaded()  # ждем загрузки страницы
    assert link_cut(href) in page.get_current_url(), "страница не соответсвует ссылке"

    # time.sleep(1)
    # assert href == page.get_current_url()


def test_count_subcategory(web_browser):  # тест подсчет колличества подкатегорий
    """ Test count subcategory. """
    page = TmallPage(web_browser)  # загружаем страницу и авторизируемся через cookiе
    page.category_button.click()  # нажимаем на элемент категории
    assert page.subsections.count() == 13  # проверяем колличество категории
    for i in page.subsections.get_text():  # проверяем что категории имеют названия
        print(i)
        assert len(i) > 0

