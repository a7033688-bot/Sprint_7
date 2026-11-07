import allure
import requests
from constant import url, order_creation


class TestObtainingOrderList:

    @allure.title('проверка что при просмотре всех заказов приходит список заказов')
    def test_check_that_when_viewing_all_orders_list_of_orders_is_displayed(self):
        response = requests.get(url + order_creation)
        assert response.status_code == 200
        assert 'orders' in response.text


