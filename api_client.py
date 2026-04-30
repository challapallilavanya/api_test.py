import requests
from config import BASE_URL, PROJECT_ID, HEADERS

class APIClient:
    def __init__(self, base_url=BASE_URL, project_id=PROJECT_ID, headers=HEADERS):
        self.base_url = base_url
        self.project_id = project_id
        self.headers = headers

    def endpoint(self, endpoint, record_id=None):
        url = f"{self.base_url}/{endpoint}"
        if record_id:
            url = f"{url}/{record_id}"
        return url
    def send_request(self, method, endpoint, payload=None):
        url = self.endpoint(endpoint)
        return requests.request(method=method, url= url, headers= self.headers, json=payload)
    def get_products(self):
        return self.send_request("GET", "products")
    def update_product(self, record_id, payload):
        return self.send_request("PUT", "products", payload)
    def delete_product(self, record_id):
        return self.send_request("DELETE", "products")
    def create_product(self, payload):
        return self.send_request("POST", "products", payload)
            