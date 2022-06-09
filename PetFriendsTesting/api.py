import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from settings import valid_email, valid_password
class PetFriends :
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self,email , password): #
        headers = {
            'email' : email,
            'password' : password
        }
        res = requests.get(self.base_url+'api/key', headers = headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def get_list_of_pets(self,auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pets(self, auth_key : json, name : str, animal_type: str,
                     age: str, pet_photo: str): #pet_photo: str
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, "rb"), 'image/jpg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delet_pet(self, auth_key: json, pet_id : str):
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает статус запроса и
        и результат в формате JSON  с текстом уведомления об успешном удалении."""
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url+'api/pets/'+ pet_id, headers=headers)
        status = res.status_code
        result = " "
        try:
            result = res.json()
        except :
            result = res.text
        return status, result

    def update_pet_info(self,auth_key: json, pet_id: str , name : str, animal_type:str, age: int):
        """Метод отправляет запрос на сервер о обновлении данных питомца по указанному ID и возвращает статус
        запроса и result в формате JSON с обновленными данными питомца"""
        headers = {'auth_key' : auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }
        res = requests.put(self.base_url + 'api/pets/'+ pet_id, headers = headers, data = data)
        status = res.status_code
        result = " "
        try:
            result = res.json()
        except:
            result = res.text
        return status ,  result
    def add_info_new_pet(self,auth_key : json, name : str, animal_type : str, age : int):
        """Метод отправляет (постит) на сервер данные о добавляемом питомце без фото и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""
        data = MultipartEncoder(
            fields={
                'name' : name,
                'animal_type' : animal_type,
                'age' : age
            })
        headers = {'auth_key' : auth_key["key"], 'Content-Type': data.content_type}
        res = requests.post(self.base_url+'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = " "
        try:
            result = res.json()
        except:
            result = res.text
        return status,  result
    def add_pet_photo(self, auth_key :json, pet_id : str, pet_photo :str):
        """Метод отправляет (постит) на сервер данные фото питомца и возвращает статус
                запроса на сервер и результат в формате JSON с данными добавленного питомца"""
        data = MultipartEncoder(
            fields={
            'pet_photo': (pet_photo, open(pet_photo, "rb"), 'image/jpg')

        })
        headers = {'auth_key' : auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = " "
        try:
            result = res.json()
        except:
            result = res.text
        return status , result



