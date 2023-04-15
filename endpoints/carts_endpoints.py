import json

from base.base_api import BaseApi


class Carts(BaseApi):
    endpoint = '/carts'
    user_endpoint = '/user'

    def get_cart_by_index(self, url, cart_id):
        response = self.get_request(url + self.endpoint + '/' + str(cart_id))
        self.check_status_code(response, 200)
        self.check_response_body_by_json_value(response, 'id', 5)
        self.check_response_body_by_json_value(response, 'userId', 3)

    def get_limited_results(self, url, params):
        response = self.get_request(url + self.endpoint, params)
        self.check_status_code(response, 200)
        self.check_carts_data_by_length(response.json(), 5)

    def create_new_cart(self, url, json_data, token):
        response = self.post_request(url + self.endpoint, json_data, token)
        self.check_status_code(response, 200)

    def get_sorted_result(self, url, params):
        response = self.get_request(url + self.endpoint, params)
        self.check_status_code(response, 200)
        self.check_carts_data_by_length(response.json(), 7)

    def get_in_date_range(self, url, params):
        response = self.get_request(url + self.endpoint, params)
        self.check_status_code(response, 200)
        self.check_carts_data_by_length(response.json(), 7)

    def update_cart(self, url, cart_id, json_data, headers):
        response = self.put_request(url + self.endpoint + '/' + str(cart_id), json_data, headers)
        self.check_status_code(response, 200)
        self.check_response_body_by_json_value(response,'userId', 3)

    def update_specific_element(self, url, cart_id, json_data, headers):
        json_data["userId"] = 5
        response = self.patch_request(url + self.endpoint + '/' + str(cart_id), json_data, headers)
        self.check_status_code(response, 200)
        self.check_response_body_by_json_value(response, 'userId', 5)

    def check_carts_data_by_length(self, data, length):
        assert len(data) == length

    def delete_cart(self, url, cart_id, headers):
        response = self.delete_request(url + self.endpoint + '/' + str(cart_id), headers=headers)
        self.check_status_code(response, 200)

    def get_user_cart(self, url, user_id, params):
        response = self.get_request(url + self.endpoint + self.user_endpoint + '/' + str(user_id), params)
        self.check_status_code(response, 200)
        self.check_carts_data_by_length(response.json(), 1)
