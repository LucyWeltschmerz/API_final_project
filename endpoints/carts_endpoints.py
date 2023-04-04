from base.base_api import BaseApi


class Carts(BaseApi):
    endpoint = '/carts'
    product_endpoint = '/carts/7'

    def create_new_cart(self, url, json_data, token):
        response = self.post_request(url + self.endpoint, json_data, token)
        self.check_status_code(response, 200)
        print(response.status_code)

    def get_sorted_result(self, url, params):
        response = self.get_request(url + self.endpoint, params)
        self.check_status_code(response, 200)
        print(response.status_code)
        print(response.text)

    def update_product(self, url, json_data, headers):
        response = self.put_request(url + self.product_endpoint, json_data, headers)
        self.check_status_code(response, 200)
        assert response.json() == {'id': 7, 'userId': 3, 'date': '2023-02-03'}

    def update_specific_element(self, url, json_data):
        json_data["userId"] = 5
        response = self.patch_request(url + self.product_endpoint, json_data)
        self.check_status_code(response, 200)
        json_response = json.loads(response.content)
        expected_userID = 5
        assert int(json_response["userId"]) == expected_userID