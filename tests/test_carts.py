import pytest
from endpoints.carts_endpoints import Carts
from utils.jsonmodels import convert_to_json


def test_create_new_cart(app_config):
    carts = Carts()
    headers = {"Authorization": app_config.token}
    json = convert_to_json.add_new_cart(15, '2023-01-02', [{"productId":5,"quantity":1},{"productId":1,"quantity":5}])
    carts.create_new_cart(app_config.base_url, json, headers)

