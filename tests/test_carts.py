import pytest
from endpoints.carts_endpoints import Carts
from utils.jsonmodels import convert_to_json


def test_create_new_cart(app_config):
    carts = Carts()
    headers = {"Authorization": app_config.token}
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
    headers = {"Authorization": app_config.token}
    params = {
        "startdate": "2019-12-10",
        "enddate": "2020-10-10"
    }
    response = carts.get_request(app_config.base_url + carts.endpoint, params, headers)
    carts.check_status_code(response, 200)
    data = response.json()
    assert len(data) == 7
    
    
    
def test_limit_results(app_config):
    carts = Carts()
    headers = {"Authorization": app_config.token}
    params = {
        "limit": "5",
        "startdate": "2019-12-10",
        "enddate": "2020-10-10"
    }
    response = carts.get_request(app_config.base_url + carts.endpoint, params, headers)
    carts.check_status_code(response, 200)
    data = response.json()
    assert len(data) == 5

    
def test_get_single(app_config):
    carts = Carts()
    headers = {"Authorization": app_config.token}
    params = None
    path_param = "/5"
    response = carts.get_request(app_config.base_url + carts.endpoint + path_param, params, headers)
    carts.check_status_code(response, 200)
    data = response.json()
    value = data["userId"]
    assert value == 3


def test_update_product(app_config):
    carts = Carts()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    json = convert_to_json.add_new_cart(3, "2023-02-03", [{"userId": 3}, { "date": 2019-12-10},
                                                          {"products": [{"productId": 1, "quantity": 3}]}])
    carts.update_product(app_config.base_url, json, headers)

def test_update_specific_element(app_config):
    carts = Carts()
    json_data = {
                    "userId": 4,
                    "date": "2019-12-10",
                    "products": [{"productId": 1, "quantity": 3}]
                    }
    carts.update_specific_element(app_config.base_url, json_data)