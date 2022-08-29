import json

url_base = "https://tmall.ru/"
url_auth = "https://login.aliexpress.ru/"
number_phone_user = '901 799-55-12'
id_user_tmall = '7-9017995512'
valid_email_tmall_page = 'dolim72899@galotv.com'
valid_password_tmall_page = '888*888'
invalid_email = 'yayob84745@submic.com'
invalid_password = 'yayob84745'
language = ['Сайт на русском\nSite Brasil (Português)\nSitio en español\nSite France\nStrona Polska'
            '\nאתר ישראלי (בעברית)\nSite Italia (Italiano)\nSite Türkiye (Türk)\nDeutsch\n한국어\nالموقع العربية']


def generate_string(n):
    return "x" * n


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def link_cut(link):
    i = str(link)
    i = i.split('?')
    i = i[0]
    return i


cookie_tmall = json.load(open("cookie_tmall.txt", "rb"))
