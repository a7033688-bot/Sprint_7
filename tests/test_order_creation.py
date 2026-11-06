import allure
import copy
import pytest
import requests
from constant import url, order_creation,list


class TestOrderCreation:

    @allure.step('выбор цвета при оформлений заказа')
    @pytest.mark.parametrize('colors', [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_color_selection_when_placing_an_order(self,colors):
        payload = copy.deepcopy(list)
        payload['color'] = colors
        response = requests.post(url + order_creation, json=payload)
        assert response.status_code == 201

    @allure.step('в ответ на создание заказа приходит track')
    def test_in_response_to_creating_an_order_you_will_receive_tracking_number(self):
        payload = copy.deepcopy(list)
        response = requests.post(url + order_creation, json=payload)
        assert response.status_code == 201
        assert 'track' in response.text 

         