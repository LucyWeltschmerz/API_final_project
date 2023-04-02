from base.base_api import BaseApi


class Carts(BaseApi):
    endpoint = '/carts'

    def create_new_cart(self, url, json_data, token):
        response = self.post_request(url + self.endpoint, json_data, token)
        self.check_status_code(response, 200)
        print(response.status_code)

    def get_sorted_result(self, url, params):
        response = self.get_request(url + self.endpoint, params)
        self.check_status_code(response, 200)
        print(response.status_code)
        print(response.text)
