import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# python -m pytest -v --driver Chrome --driver-path C:\chromedriver_win32\chromedriver.exe test_selenium_petfriends_1.py


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets(driver):
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('yayob84745@submic.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('yayob84745')

    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()


    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
    pytest.driver.find_element_by_xpath('//a[@href="/my_pets"]').click()


   
    # находим элементы на странице со статистикой пользователя
    pets_statistic = pytest.driver.find_elements_by_xpath('//div[@class=".col-sm-4 left"]')

    # находим элементы на странице с фотографиями питомцев
    images = pytest.driver.find_elements_by_xpath('//img[@style="max-width: 100px; max-height: 100px;"]')

    # находим элементы на странице с каточками питомцев
    # cards = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr')
    cards = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))
    count_cards = len(cards)

    driver.implicitly_wait(5)

    names = pytest.driver.find_elements_by_xpath('//td[1]')    # находим элементы на странице с именами питомцев
    breeds = pytest.driver.find_elements_by_xpath('//td[2]')    # находим элементы на странице с породой питомцев
    age = pytest.driver.find_elements_by_xpath('//td[3]')    # находим элементы на странице с возрастом питомцев

    names_list = []    #список с именами всех питомцев
    for i in names:
        res = i.text
        names_list.append(res)    # добавляем в список names_list имя питомца из цикла
    print(names_list)

    breeds_list = []    #список с породой всех питомцев
    for i in breeds:
        res = i.text
        breeds_list.append(res)    # добавляем в список breeds_list породу питомца из цикла
    print(breeds_list)

    age_list = []   # список с возрастом всех питомцев
    for i in age:
        res = i.text
        age_list.append(res)   # добавляем в список age_list возраст питомца из цикла
    print(age_list)

    # Получаем количество питомцев из данных статистики
    number = pets_statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # проверка колличество питомцев в статистике равно колличеству карточек
    assert len(images) == number and count_cards == number, print(len(images))
    print(count_cards)

    pets_without_image = 0   # счетчик случаев когда нет аттрибута 'src'
    for i in range(len(cards)):
        assert names[i].text != '', 'у питомца отсутствует имя'    # проверяем что у питомца присутствует имя
        assert breeds[i].text != '', ' у питомца отсутсвует порода'    # проверяем что у питомца присутствует порода
        assert age[i].text != '', ' у питомца отсутсвует возраст'    # проверяем что у питомца присутствует возраст
        print(names_list.count(names[i].text))


        if images[i].get_attribute('src') == "":  #  если аттрибут 'src' равен пустой строке '' тогда прибавляем к счетчику +1
            pets_without_image += 1
            #если имя порода и возраст больше чем в одном екземпляре тогда делаем проверку и выводим сообщение есть одинаковые питомцы
        # if names_list.count(names[i].text) > 1 and breeds_list.count(breeds[i].text) > 1 and age_list.count(age[i].text) > 1:
        assert names_list.count(names[i].text) == 1 and breeds_list.count(breeds[i].text) == 1 and age_list.count(age[i].text) == 1,'есть одинаковые питомцы'
        # иначе проверяем по отдельности на наличие повторяющихся имен , породы , и возраста
        #else:
        assert names_list.count(names[i].text) == 1, 'присутствуют питомцы с одинаковым именем'    # проверяем что имя
        # питомца из цыкла входит в список names_list один раз иначе есть питомцы с одинаковыми именами
        assert breeds_list.count(breeds[i].text) == 1, 'присутствуют питомцы с одинаковой породой'  # проверяем что порода
        # питомца из цыкла входит в список breeds_list один раз иначе есть питомцы с одинаковой породой
        assert age_list.count(age[i].text) == 1, 'присутствуют питомцы с одинаковым возрастом'  # проверяем что возраст
        # питомца из цыкла входит в список age_list один раз иначе есть питомцы с одинаковым возрастом


    # проверка число случаев отсутсвия аттрибута 'src' должно быть меньше либо равно половины колличества питомцев
    assert pets_without_image <= number/2









