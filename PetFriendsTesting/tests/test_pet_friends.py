import os.path

from api import PetFriends
from settings import valid_email, valid_password , invalid_email, invalid_password , invalid_api_key



pf = PetFriends()

def test_get_api_for_valid_user(email = valid_email, password = valid_password):
    """Проверяем что запрос api ключа возвращает статус 200 и в результате содержит слово key"""
    status, result = pf.get_api_key(email,password) # отправляем запрос api ключа, возвращает статус 200
    # и в тесте содержится слово key
    assert status == 200 # сверяем статус код
    assert 'key' in result # сверяем наличие  'key' в result
    print(result)
def test_get_api_for_invalid_user(email = invalid_email, password = invalid_password):
    """ Негативный тест.Проверяем что запрос api ключа возвращает статус 400 при использовании невалидных данных
     email и password,
    и в результате отсутствует слово key"""
    status, result = pf.get_api_key(email,password) # отправляем запрос api ключа, возвращает статус 200
    # и в тесте содержится слово key
    assert 400 <= status < 500 # сверяем, статус код должен быть 4ХХ
    assert 'key' not in result # сверяем  отсутствие  'key' в result


def test_get_all_pets_with_valid_key(filter=""):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key.Далее используя этот ключ
    запрашиваем список всех питомцев и  проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо  ' '   """
    _,  auth_key = pf.get_api_key(valid_email,valid_password)#запрашиваем api ключ и сохраняем в переменную auth_key
    status, result = pf.get_list_of_pets(auth_key, filter)#запрашиваем список всех питомцев
    assert status == 200 # сверям статус
    assert len(result['pets']) > 0 #  проверяем что список не пустой
def test_get_all_pets_with_invalid_key(filter=""):
    """Негативный тест. Проверяем что запрос возвращает статус 4ХХ , при использовании невалидного api ключа"""

    auth_key = invalid_api_key # используем невалдный  api ключ с ошибкой в значении
    # {"key" : "f4dc479e3b03b0641574eef89a034ee99d9f554a8119cf8d23139d2d-"}

    status, result = pf.get_list_of_pets(auth_key, filter)
    assert  400 <= status < 500 # сверяем, статус код должен быть 4ХХ


def test_add_new_pet_with_valid_data(name='барбоса ',animal_type='барборис ', age='2 ',pet_photo='images/dog2.jpg' ): #pet_photo='images/dog1.jpg'
    """Проверяем что можно добавить питомца с корректными данными"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)  # получем полный путь изображения питомца и сохраняем
    #  в переменную pet_photo
    _, auth_key = pf.get_api_key(valid_email, valid_password)  #запрашиваем api ключ и сохраняем в переменную auth_key
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)  # pet_photo
    assert status == 200  # сверяем статус
    assert result['name'] == name # и имя питомца соответствует заданному


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""
    #Получаем ключ auth_key  и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len( my_pets['pets']) == 0:
        pf.add_new_pets(auth_key, "001", "001", "1" , " images/dog1.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'] [0] ["id"]
    status, _ = pf.delet_pet(auth_key,pet_id)
    # ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем что статус ответа равен 200  и в списке питомцев нет id  удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info_valid_data(name='UP',animal_type="DATE", age=3):
    """Проверяем возможность обновления информации о питомце"""
    _ , auth_key = pf.get_api_key(valid_email, valid_password)#получаем ключ auth_key
    _ , my_pets = pf.get_list_of_pets(auth_key,"my_pets")#  и список питомцев

    if len(my_pets['pets']) > 0: # если список не пустой пробуем обновить его имя, тип и возраст
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200 # Проверяем что статус ответа 200
        assert result['name'] == name # и имя питомца соответствует заданному
    else:
        raise Exception("There is no my pets") #если список питомцев пустой , то выкидываем исключение с текстом
    # об отсутствии своих питомцев


def test_successful_update_self_pet_info_invalid_data(name='UP', animal_type="DATE", age="abc"):
    """Проверяем возможность обновления информации о питомце при использовании невалидного параметра age='abc' """
    _, auth_key = pf.get_api_key(valid_email, valid_password)#получаем ключ auth_key
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")#  и список питомцев

    if len(my_pets['pets']) > 0:  # если список не пустой пробуем обновить его имя, тип и возраст
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200  # Проверяем что статус ответа 200
        assert int(result['age']) == int(age)  # Проверяем что в поле возраст только числа . BAG в параметре возраст
        # можно передать буквы и программа не выдает ошибку, на странице отображается питомец с буквами в поле возраст
    else:
        raise Exception("There is no my pets")  #если список питомцев пустой , то выкидываем исключение с текстом
    # об отсутствии своих питомцев

def test_add_info_new_pet_without_photo_valid_data(name = "NEW", animal_type = "INFO", age = "1"):
    """Проверяем что можно добавить информацию о питомце с корректными данными без фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password) #запрашиваем api ключ и сохраняем в переменную auth_key
    status, result = pf.add_info_new_pet(auth_key, name, animal_type, age)
    assert status == 200  # Проверяем что статус ответа 200
    assert result['name'] == name  # и имя питомца соответствует заданному

def test_add_info_new_pet_without_photo_invalid_data(name = "NEW", animal_type = "INFO", age = "abc"):
    """Проверяем что можно добавить информацию о питомце с не корректными данными ( в параметре возраст отправить
    буквы вместо цифр  age = 'abc'  """
    _, auth_key = pf.get_api_key(valid_email, valid_password) #запрашиваем api ключ и сохраняем в переменную auth_key
    status, result = pf.add_info_new_pet(auth_key, name, animal_type, age)
    assert status == 200  # Проверяем что статус ответа 200
    assert result['name'] == name  # и имя питомца соответствует заданному
    assert int(result['age']) == int(age)  # Проверяем что в поле возраст только числа . BAG в параметре возраст
    # можно передать буквы и программа не выдает ошибку, на странице отображается питомец с буквами в поле возраст

def test_add_pet_photo_valid_data( pet_photo = 'images/dog1.jpg'):
    """Проверяем что можно добавить фото питомца с корректными данными """
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)  # получем полный путь изображения питомца и сохраняем
    _, auth_key = pf.get_api_key(valid_email, valid_password) #запрашиваем api ключ и сохраняем в переменную auth_key
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len( my_pets['pets']) == 0:
        pf.add_info_new_pet(auth_key, name='dog1', animal_type='dog1', age='1')
        _,my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    # Берём id первого питомца из списка
    pet_id = my_pets['pets'][0]["id"]
    status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)
    # ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем что статус ответа равен 200  и в списке питомцев нет id  удалённого питомца
    assert status == 200 # Проверяем что статус ответа 200
    assert len(result['pet_photo']) > 0  # Проверяем добавилось ли фото


def test_add_pet_photo_valid_data( pet_photo = 'images/1.png'):
    """Проверяем что можно добавить фото (в формате   .png) питомца с корректными данными """
    pet_photo = os.path.join(os.path.dirname(__file__),pet_photo)  # получем полный путь изображения питомца и сохраняем
    _, auth_key = pf.get_api_key(valid_email, valid_password) #запрашиваем api ключ и сохраняем в переменную auth_key
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len( my_pets['pets']) == 0 :
        pf.add_info_new_pet(auth_key, name='dog1', animal_type='dog1', age='1')
        _,my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    # Берём id первого питомца из списка
    pet_id = my_pets['pets'][0]["id"]
    status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)
    # ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем что статус ответа равен 200
    assert status == 200 # Проверяем что статус ответа 200  , выдает статус код 500   """bag нельзя добавть фото в профиль в формате png"""
    assert len(result['pet_photo']) > 0 # Проверяем добавилось ли фото
    """bag нельзя добавить фото в профиль в формате png"""










