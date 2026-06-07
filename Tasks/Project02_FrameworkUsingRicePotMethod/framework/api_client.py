import requests

class APIClient:
    def __init__(self, base_url='https://reqres.in/api'):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        return requests.get(f'{self.base_url}{endpoint}')

    def post(self, endpoint, data=None, json=None):
        return requests.post(f'{self.base_url}{endpoint}', data=data, json=json)

    def put(self, endpoint, data=None, json=None):
        return requests.put(f'{self.base_url}{endpoint}', data=data, json=json)

    def delete(self, endpoint):
        return requests.delete(f'{self.base_url}{endpoint}')