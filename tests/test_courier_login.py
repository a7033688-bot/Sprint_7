import allure
import requests
from helpers import register_new_courier_and_return_login_password
from constant import url, courier_is_available_in_system, delete_courier


class TestCourierLogin:

    @allure.step('проверка что курьер может авторизоватся')
    def test_courier_can_log_in(self):
        new_courier = register_new_courier_and_return_login_password()
        payload = {}
        payload['login'] = new_courier[0]
        payload['password'] = new_courier[1]
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 200
        id = str(response.json()['id'])
        delete = requests.delete(url + delete_courier + id)
        assert delete.status_code == 200

    @allure.step('успешный запрос возвращает id')
    def test_after_request_is_successfully_completed_an_identifier_is_returned(self):
        new_courier = register_new_courier_and_return_login_password()
        payload = {}
        payload['login'] = new_courier[0]
        payload['password'] = new_courier[1]
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 200
        assert 'id' in response.text
        id = str(response.json()['id'])
        delete = requests.delete(url + delete_courier + id)
        assert delete.status_code == 200

    @allure.step('негативная проверка. не получится авторизоватся если нет поля логин')
    def test_you_won_be_able_to_log_in_if_there_no_login_field(self):
        new_courier = register_new_courier_and_return_login_password()
        payload = {}
        payload['password'] = new_courier[1]
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 400
        payload = {}
        payload['login'] = new_courier[0]
        payload['password'] = new_courier[1]
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 200
        id = str(response.json()['id'])
        delete = requests.delete(url + delete_courier + id)
        assert delete.status_code == 200

    @allure.step('негативная проверка. не получится авторизоватся если нет поля пароль')
    def test_you_won_be_able_to_log_in_if_there_no_password_field(self):
        new_courier = register_new_courier_and_return_login_password()
        payload = {}
        payload['login'] = new_courier[0]
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 400
        payload = {}
        payload['login'] = new_courier[0]
        payload['password'] = new_courier[1]
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 200
        id = str(response.json()['id'])
        delete = requests.delete(url + delete_courier + id)
        assert delete.status_code == 200

    @allure.step('негативная проверка. если ввести логин не правильно появится ошибка')
    def test_if_you_enter_login_incorrectly_an_error_will_appear(self):
        new_courier = register_new_courier_and_return_login_password()
        payload = {}
        payload['login'] = 'pract'
        payload['password'] = new_courier[1]
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 404
        payload = {}
        payload['login'] = new_courier[0]
        payload['password'] = new_courier[1]
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 200
        id = str(response.json()['id'])
        delete = requests.delete(url + delete_courier + id)
        assert delete.status_code == 200

    @allure.step('негативная проверка. если ввести пароль не правильно появится ошибка')
    def test_if_you_enter_password_incorrectly_an_error_will_appear(self):
        new_courier = register_new_courier_and_return_login_password()
        payload = {}
        payload['login'] = new_courier[0]
        payload['password'] = '12345'
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 404
        payload = {}
        payload['login'] = new_courier[0]
        payload['password'] = new_courier[1]
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 200
        id = str(response.json()['id'])
        delete = requests.delete(url + delete_courier + id)
        assert delete.status_code == 200

    @allure.step('если авторизоватся с несуществующем профилем вернется ошибка')
    def test_if_you_log_in_as_non_existent_user_request_returns_an_error(self):    
        payload = {}
        payload['login'] = 'texas'
        payload['password'] = '12345'
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 404
        



    
    
