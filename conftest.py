import pytest
import requests
import copy
from constant import delete_courier, courier_is_available_in_system, url
from courier import register_new_courier_and_return_login_password



@pytest.fixture
def clear():
    new_courier = register_new_courier_and_return_login_password()
    payload = {}
    payload['login'] = new_courier[0]
    payload['password'] = new_courier[1]
    payload['firstName'] = new_courier[2]
    payload_1 = copy.deepcopy(payload)
    yield payload
    response = requests.post(url + courier_is_available_in_system,data=payload_1)
    assert response.status_code == 200
    id = str(response.json()['id'])
    delete = requests.delete(url + delete_courier + id)
    assert delete.status_code == 200
    


