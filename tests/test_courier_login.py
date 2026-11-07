import allure
import pytest
import requests
from constant import url, courier_is_available_in_system, delete_courier


@pytest.mark.usefixtures("clear")
class TestCourierLogin:

    @allure.title('проверка что курьер может авторизоватся')
    def test_courier_can_log_in(self,clear):
        payload = clear
        del payload['firstName']
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 200
        assert 'id' in response.text

    @allure.title('успешный запрос возвращает id')
    def test_after_request_is_successfully_completed_an_identifier_is_returned(self,clear):
        payload = clear
        del payload['firstName']
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 200
        assert 'id' in response.text
        

    @allure.title('негативная проверка. не получится авторизоватся если нет поля логин')
    def test_you_won_be_able_to_log_in_if_there_no_login_field(self,clear):
        payload = clear
        del payload['firstName']
        del payload['login']
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 400
        assert 'Недостаточно данных для входа' in response.text

    @allure.title('негативная проверка. не получится авторизоватся если нет поля пароль')
    def test_you_won_be_able_to_log_in_if_there_no_password_field(self,clear):
        payload = clear
        del payload['firstName']
        del payload['password']
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 400
        assert 'Недостаточно данных для входа' in response.text

    @allure.title('негативная проверка. если ввести логин не правильно появится ошибка')
    def test_if_you_enter_login_incorrectly_an_error_will_appear(self,clear):
        payload = clear
        payload['login'] = 'pract'
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 404
        assert 'Учетная запись не найдена' in response.text

    @allure.title('негативная проверка. если ввести пароль не правильно появится ошибка')
    def test_if_you_enter_password_incorrectly_an_error_will_appear(self,clear):
        payload = clear 
        payload['password'] = '12345'
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 404
        assert 'Учетная запись не найдена' in response.text
        

    @allure.title('если авторизоватся с несуществующем профилем вернется ошибка')
    def test_if_you_log_in_as_non_existent_user_request_returns_an_error(self):    
        payload = {}
        payload['login'] = 'texas'
        payload['password'] = '12345'
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 404
        assert 'Учетная запись не найдена' in response.text
        



    
    
