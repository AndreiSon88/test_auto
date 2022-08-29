#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os, time
import pickle

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

from config import url_base, url_auth ,cookie_tmall



class TmallPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or url_base
            super().__init__(web_driver, url)

            web_driver.get(url_base)
            for cookie in cookie_tmall:   #pickle.load(open("cookies","rb"))
                web_driver.add_cookie(cookie)

            web_driver.refresh()
            time.sleep(5)




        time.sleep(3)

    enter_btn_login = WebElement(css_selector="button[type='submit'")
    # logo aliexpress
    logo_ali = WebElement(xpath='//a')
    # логотип страницы tmall
    logo_tmall = WebElement(xpath='//*[@class="logo-base"]')
    gif_logo_tmall = WebElement(xpath='//*[@class="logo-gif"]')



    # user_account_info_icon
    user_account_info_icon = WebElement(xpath='//*[@class="user-account-info"]')
    # my_aliexpress_link
    my_aliexpress_link = WebElement(xpath='//span/a[contains(text(),"Мой AliExpress")]')
    # my_aliexpress_menu
    my_aliexpress_menu = WebElement(xpath='//li/a[contains(text(),"Мой AliExpress")]')
    # global_site_link
    global_site_link = WebElement(xpath='//div/a[contains(text(),"Go to Global Site (English)")]')
    # Buyer Protection - защита покупателя
    bayer_protection = WebElement(xpath='//*[@class="ng-item ng-bp"]/a')
    # info bayer protection
    info_bayer_protection = ManyWebElements(xpath='//*[@class="Group--groupContainer--2Qw6qft "]')
# test_get_support
    # menu_help -  выпадающее меню помощь
    menu_help = WebElement(xpath='//*[@class="ng-sub-title"]')
    # support - техподдержка
    support = WebElement(xpath='//*[@class="ng-help-link"]')
    # logo_help_centr - логотип центра помощи
    logo_help_centr = WebElement(xpath='//*[@class="header-title-3Y6O"]')
                # # споры и жалобы
                # disputes_and_complaints = WebElement(xpath='//*[@data-role="complaint-link"]')
#  test_get_online_chat
    # online_chat -
    online_chat = WebElement(xpath='//*[contains(text(),"Онлайн чат")]')
    # helper_avatar
    helper_avatar = WebElement(xpath='//*[@class="Avatar Avatar--md Avatar--circle"]')
    # # background_login елемент страницы авторизации
    # background_login = WebElement(id="root")
# test_get_warranty
    # warranty
    warranty = WebElement(xpath='//*[contains(text(),"Гарантии")]')
# language - язык страницы
    language = WebElement(id='switcher-language-info')

# contain_language - блок языков
    contain_language = ManyWebElements(xpath='//*[@class="switcher-site-list"]')
    # btn_language - кнопка язык
    btn_language = WebElement(xpath='//span[contains(text(),"Выбрать язык")]')
    # кнопка выбор города и языка
    menu_city_language = WebElement(xpath='//*[@class="TopHeadV2_TopHeadV2__shipTo__1c1dq"]')
    #  язык - сайт на русском
    rus = WebElement(xpath='//*[@data-locale="ru_RU"]')
    # кнопка выбор языка -  русский
    rus_msg = WebElement(xpath='//button[contains(text(),"Русский")]')

    bra = WebElement(xpath='//*[@data-locale="pt_BR"]')
    bra_msg = WebElement(xpath='//button[contains(text(),"Português")]')

    esp = WebElement(xpath='//*[@data-locale="es_ES"]')
    esp_msg = WebElement(xpath='//*[contains(text(),"Español")]')

    fra = WebElement(xpath='//*[@data-locale="fr_FR"]')
    fra_msg = WebElement(xpath='//*[contains(text(),"Français")]')
    fra_coupon = WebElement(xpath='//*[@class="CouponPopup_CouponPopup__header__13yyd"]')
    background_coopon = WebElement(xpath='//*[@class="ali-kit_Dialog__background__1lirhm"]')
    fra_coupon_ = WebElement(xpath='//*[@role="document"]/div/button')

    pol = WebElement(xpath='//*[@data-locale="pl_PL"]')
    pol_msg = WebElement(xpath='//*[contains(text(),"Polskie")]')

    tai = WebElement(xpath='//*[@data-locale="iw_IL"]')
    tai_msg = WebElement(xpath='//*[contains(text(),"עברית")]')

    itl = WebElement(xpath='//*[@data-locale="it_IT"]')
    itl_msg = WebElement(xpath='//*[contains(text(),"Italiano")]')

    turk = WebElement(xpath='//*[@data-locale="tr_TR"]')
    turk_msg = WebElement(xpath='//*[contains(text(),"Türkçe")]')

    deutesch = WebElement(xpath='//*[@data-locale="de_DE"]')
    deutesch_msg = WebElement(xpath='//*[contains(text(),"Deutsch")]')

    korea = WebElement(xpath='//*[@data-locale="ko_KR"]')    #한국어
    korea_msg = WebElement(xpath='//*[contains(text(),"한국어")]')

    arabian = WebElement(xpath='//*[@data-locale="ar_MA"]')    #العربية
    arabian_msg = WebElement(xpath='//*[contains(text(),"العربية")]')




    # my_order_menu
    my_order_menu = WebElement(xpath='//li/a[contains(text(),"Мои заказы")]')
    # message_center_menu
    message_center_menu = WebElement(xpath='//li/a[contains(text(),"Центр сообщений")]')
    # my_wishes_menu
    my_wishes_menu = WebElement(xpath='//li/a[contains(text(),"Мои желания")]')
    # favorite stores
    favorite_stores_menu = WebElement(xpath='//li/a[contains(text(),"Любимые магазины")]')
    # my_coupons_menu
    my_coupons_menu = WebElement(xpath='//li/a[contains(text(),"Мои купоны")]')


    # sign_in_user_account_btn - кнопка войти на Tmall
    sign_in_user_account_btn = WebElement(css_selector='a.sign-btn')

    # sign_out_user_account_btn - кнопка войти на Tmall
    sign_out_user_account_btn = WebElement(xpath='//div/a[contains(text(),"Выйти")]')

    # Search - поле поиска
    search = WebElement(id='search-key')


    # Search button - кнопка поиска
    search_run_button = WebElement(xpath='//*[@class="search-button"]')

    # Search_error - ошибка поиска
    search_error = WebElement(xpath='//*[@class="SearchWrap_SearchError__wordsWrap__oy8dw"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//*[@class="SearchProductFeed_SearchProductFeed__productFeed__tznhm"]')








    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//*[@class=]')

    # basket_icon_shoping_card - иконка корзина
    basket_icon_shoping_card = WebElement(xpath='//*[@class="nav-cart nav-cart-box"]/a')
    # basket_counter_shoping_card
    # msg_basket_without_auth
    msg_basket_empty = WebElement(xpath='//*[@class="ShoppingcartStates_CartState__container__1ww0f"]/p')
    icon_basket = WebElement(xpath='//*[@class="right-shopcart"]/a/i')
    basket_counter_shoping_card = WebElement(xpath='//span[@class="cart-number"]')
    # favorite_icon иконка избранное
    favorite_icon = WebElement(xpath='//*[@class="nav-wishlist"]/a')
# test_add_product_in_basket
    # product_wrench  ключ динамометрический в результате поиска
    product_wrench = WebElement(xpath='//*[@class="product-snippet_ProductSnippet__description__152uer"]/a')
    # product_name
    product_name = WebElement(xpath='//*[@class="Product_Name__container__hntp3"]/h1')
    # product_price
    product_price = WebElement(xpath='//*[@class="Product_Price__container__1uqb8 product-price"]/span')
    # btn_in_basket
    btn_in_basket = WebElement(xpath='//*[@class="ali-kit_Tooltip__wrapper__sht7gl"]/button')
    # list_product_in_basket
    list_product_in_basket = WebElement(xpath='//*[@class="ShoppingcartItemList_ShoppingcartItemList__storeList__tbcus"]')



# fm_login_id
    fm_login_id = WebElement(id='fm-login-id')
# fm_login_password
    fm_login_password = WebElement(id='fm-login-password')
# btn_in_login
    btn_in_login = WebElement(xpath='//*[@class="comet-btn comet-btn-primary comet-btn-large comet-btn-block login-submit"]')


# test get report copyright
    report_copyright = WebElement(xpath='//*[contains(text(),"Сообщить о нарушении авторских прав")]')

    subsections = ManyWebElements(xpath='//div[@class="rax-view categoryWrap"]')

    category_button = WebElement(xpath='//div[contains(text(), "Категории")]')
    sort_price_btn = WebElement(xpath='//button[contains(text(), "Цена")]')
    sort_price_result = ManyWebElements(xpath='//*[@class="snow-price_SnowPrice__blockMain__wuoiot"]')