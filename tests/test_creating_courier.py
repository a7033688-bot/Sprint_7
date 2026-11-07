import pytest
import allure
import copy
import requests
from constant import url, courier_is_available_in_system, delete_courier, creating_courier, PAYLOAD



@pytest.mark.usefixtures("clear")
class TestCreatingCourier:

    @allure.title('тест проверяет можно ли создать курьера')
    def test_successful_creation_of_courier(self,clear):
        payload = clear
        del payload['firstName']
        response = requests.post(url + courier_is_available_in_system, data=payload)
        assert response.status_code == 200
        assert 'id' in response.text

    @allure.title('тест проверяет что нельзя создать двух одинаковых курьеров')
    def test_it_is_impossible_to_create_two_identical_couriers(self,clear):
        payload = clear
        response = requests.post(url + creating_courier, data=payload)
        assert response.status_code == 409
        assert 'Этот логин уже используется' in response.text

    @allure.title('тест проверяет что можно создать курьера введя обязательные поля ') 
    def test_all_required_fields_must_be_specified_in_main_text(self,):
        payload = copy.deepcopy(PAYLOAD)
        response = requests.post(url + creating_courier, data=payload)
        assert response.status_code == 201
        assert 'ok' in response.text
        del payload['firstName']
        response = requests.post(url + courier_is_available_in_system, data=payload)
        if response.status_code == 200:
            id = str(response.json()['id'])
            delete = requests.delete(url + delete_courier + id)
        

    @allure.title('успешный запрос возвращает правильный текст ответа')
    def test_upon_successful_completion_of_request_correct_response_text_is_returned(self):
        payload = copy.deepcopy(PAYLOAD)
        response = requests.post(url + creating_courier, data=payload)
        assert response.text == '{"ok":true}'
        assert response.status_code == 201
        del payload['firstName']
        response = requests.post(url + courier_is_available_in_system, data=payload)
        if response.status_code == 200:
            id = str(response.json()['id'])
            delete = requests.delete(url + delete_courier + id)

    @allure.title('негативный тест. при отсутствие поля логин новый курьер не создастся')
    def test_login_field_is_missing_new_courier_will_not_be_created(self):
        payload = copy.deepcopy(PAYLOAD)
        del payload['login']
        response = requests.post(url + creating_courier, data=payload)
        assert response.status_code == 400
        assert 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('негативный тест. при отсутствие поля пароль новый курьер не создастся')
    def test_password_field_is_missing_new_courier_will_not_be_created(self):
        payload = copy.deepcopy(PAYLOAD)
        del payload['password']
        response = requests.post(url + creating_courier, data=payload)
        assert response.status_code == 400
        assert 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('негативный тест. нельзя создать двух курьеров с одинаковым логином')
    def test_cannot_be_two_couriers_with_same_login(self,clear):
        payload = clear
        response = requests.post(url + creating_courier, data= payload)
        assert response.status_code == 409 
        assert 'Этот логин уже используется' in response.text
    


    
        