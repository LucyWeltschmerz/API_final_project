import pytest
from endpoints.carts_endpoints import Carts
from utils.jsonmodels import convert_to_json

def test_get_single_cart(app_config):
    carts = Carts()
    carts.get_cart_by_index(app_config.base_url, 5)

def test_limit_results(app_config):
    carts = Carts()
    params = {
        "limit": "5",
        "startdate": "2019-12-10",
        "enddate": "2020-10-10"
    }
    carts.get_limited_results(app_config.base_url, params)

def test_create_new_cart(app_config):
    carts = Carts()
    headers = {"Authorization": app_config.token, "Content-Type": "application/json"}
    json = convert_to_json.add_new_cart(15, '2023-01-02',
                                        [{"productId": 5, "quantity": 1}, {"productId": 1, "quantity": 5}])
    carts.create_new_cart(app_config.base_url, json, headers)


def test_get_sorted_results(app_config):
    carts = Carts()
    params = {
        "sort": "desc",
        "startdate": "2000-03-15",
        "enddate": "2023-02-04"
    }
    carts.get_sorted_result(app_config.base_url, params)


def test_get_in_date_range(app_config):
    carts = Carts()
    params = {
        "startdate": "2019-12-10",
        "enddate": "2020-10-10"
    }
    carts.get_in_date_range(app_config.base_url, params)

def test_update_cart(app_config):
    carts = Carts()
    headers = {"Authorization": app_config.token, "Content-Type": "application/json"}
    json = convert_to_json.update_cart(3, "2023-02-03", {"productId": 1, "quantity": 3})
    carts.update_cart(app_config.base_url, 7, json, headers)

def test_update_specific_element(app_config):
    carts = Carts()
    headers = {"Authorization": app_config.token, "Content-Type": "application/json"}
    json_data = {
                    "userId": 4,
                    "date": "2019-12-10",
                    "products": [{"productId": 1, "quantity": 3}]
                    }
    carts.update_specific_element(app_config.base_url, 7, json_data, headers)

def test_delete_cart(app_config):
    cart = Carts()
    headers = {"Authorization": app_config.token, "Content-Type": "application/json"}
    cart.delete_cart(app_config.base_url, 6, headers)


def test_get_user_cart(app_config):
    carts = Carts()
    params = {
        "startdate": "2019-12-10",
        "enddate": "2020-10-10"
    }
    carts.get_user_cart(app_config.base_url, 2, params)
