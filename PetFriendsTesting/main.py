import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

base_url = "https://petfriends.skillfactory.ru/"
def get_list_of_pets( email, passwd):  #
    headers = {
        'email': email,
        'password': passwd
    }
    res = requests.get(base_url + 'api/key', headers=headers)
    status = res.status_code

    try:
        result = res.json()
    except:
        result = res.text
    return status, result


print(get_list_of_pets("yayob84745@tofeat.com", "yayob84745"))
