import os
import time

from config import url_auth
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class TmallLoginPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or url_auth
            super().__init__(web_driver, url)

        time.sleep(3)

 #auth locators

    # login_btn - кнопка ВХОД на странице https://login.aliexpress.ru
    login_btn = WebElement(xpath='//div[@class="ali-kit_Tab__tab__3np7b9 batman-v2_batman__tab__bbyedu"]/span')
    # login input field - поле ввода "email"
    login_input_field = WebElement(id="email")
    # password_input_field - поле ввода "password"
    password_input_field = WebElement(id="password")
    # кнопка войти на странице https://login.aliexpress.ru
    enter_btn_login = WebElement(css_selector="button[type='submit'")
    # кнопка выйти на странице Tmall
    sign_out_user_account_btn = WebElement(xpath=('//*[@class="flyout-user-signout"]/a'))
    # incorrect_data_msg - сообщение "некорректные учетные данные"
    incorrect_data_msg = WebElement(xpath='//div[@class="ali-kit_Input__wrapper__cjj0j4 wrapper_m"]/span')
    # email_format_field_error_msg - сообщение "Почта должна быть формата username@domain.ru"
    email_format_field_error_msg = WebElement(xpath='//*[@class="ali-kit_Input__wrapper__cjj0j4 wrapper_m"]/span')
    # password_format_field_error_msg - сообщение "Что-то пошло не так"
    password_format_field_error_msg = WebElement(xpath='//*[@class="ali-kit_Input__wrapper__cjj0j4 wrapper_m"]/span')
    # recovery_login_string
    recovery_password_str_link = WebElement(xpath='//a[contains(text(), "Забыли пароль?")]')
    logo_aliexpress = WebElement(xpath='//*[@class="logo"]/a')
    logo_recovery_password = WebElement(xpath='//*[@class="logo-title"]')

    # login_with_phone_number - вход с помошью телефона
    login_with_phone_number_str_link = WebElement(xpath='//*[@class="email-auth_EmailAuth__form__1p9j8j"]/div/span')
    # numbers_phone_input_field - поле ввода номера телефона
    numbers_phone_input_field = WebElement(css_selector='input.snow-ali-kit_Input__inputField__1aiyxh')

    # get_the_code_btn - кнопка получить код
    get_the_code_btn = WebElement(xpath='//button[@data-spm-anchor-id="a2g2w.verification_by_phone.0.i14.59824aa6cUVXRh"]')
    input_code_field = WebElement(xpath='//div[@data-spm-anchor-id="a2g2w.verification_by_phone.0.i21.59824aa6cUVXRh"]')

    # instruction_btn
    instr_social_login_btn = WebElement(xpath='//*[@class="BatmanWidget_SnsInformer__snsInformerContent__1c134"]/a')

    # info_user_contract - служебная информация пользователя под иконками соц сетей
    info_user_contract = WebElement(xpath = '//span[contains(text(), "Регистрируясь на AliExpress или авторизуясь через социальные сети, вы соглашаетесь с ")]' )
    # ok_btn - кнопка ссылка на страницу авторизации ok
    ok_btn = WebElement(xpath='//*[@class="sns_OldSns__oldIcon__e9laja"]/img[@alt="ok"]')
    # vk_btn - кнопка ссылка на страницу авторизации vk
    vk_btn = WebElement(xpath='//img[@alt="vk"]')
    # google_btn -  кнопка ссылка на страницу авторизации  google
    google_btn = WebElement(xpath='//img[@alt="google"]')
    # mailru_btn - кнопка ссылка на страницу авторизации mail.ru
    mailru_btn = WebElement(xpath='//img[@alt="mailru"]')
    # confidentional_link - ссылка конфиденциальность в подвале страницы
    confidentional_link = WebElement(xpath='//a[contains(text(), "Политика Конфиденциальности")]')
    # map_link ссылка карта сайта в подвале страницы
    map_link = WebElement(xpath='//a[contains(text(), "Карта сайта")]')
    # logo_ali_on_login - логотип aliexpress на странице "https://login.aliexpress.ru"
    logo_ali_on_login = WebElement(xpath ='//*[@class="Header_SearchSection__container__s795p"]/div/a')