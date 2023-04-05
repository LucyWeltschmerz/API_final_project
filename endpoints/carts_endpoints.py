import json

from base.base_api import BaseApi


class Carts(BaseApi):
    endpoint = '/carts'
    product_endpoint = '/carts/1'

    def create_new_cart(self, url, json_data, token):
        response = self.post_request(url + self.endpoint, json_data, token)
        self.check_status_code(response, 200)
        print(response.status_code)
        print(response.text)

    def get_sorted_result(self, url, params):
        response = self.get_request(url + self.endpoint, params)
        self.check_status_code(response, 200)
        print(response.status_code)
        print(response.text)

    def update_product(self, url, json_data, headers):
        response = self.put_request(url + self.product_endpoint, json_data, headers)
        self.check_status_code(response, 200)
        print("response-body: ", response.text)
        self.check_response_body_by_json_value(response,'userId', 3)

    def update_specific_element(self, url, json_data, headers):
        json_data["userId"] = 5
        response = self.patch_request(url + self.product_endpoint, json_data, headers)
        self.check_status_code(response, 200)
        print(response.json())

    def check_carts_data_by_length(self, data, length):
        assert len(data) == length