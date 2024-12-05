import requests

class APIConnector:
    def __init__(self, base_url, api_key, api_secret):
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret

    def fetch_data(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}:{self.api_secret}"}
        response = requests.get(url, headers=headers)
        if response.ok:
            return response.json()
        else:
            raise Exception(f"API request failed: {response.status_code}, {response.text}")
