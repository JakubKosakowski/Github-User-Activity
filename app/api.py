import requests
from requests.exceptions import HTTPError, Timeout

class APIHandler():
    def __init__(self, api_base_url="https://api.github.com", token=None):
        self.api_base_url = api_base_url
        self.token = token

    def _get_headers(self):
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Python-GitHubAPI"
        }
        if self.token:
            headers['Authorization'] = f"Bearer {self.token}"
        return headers
    
    def get_user_info(self, username):
        url = f'{self.api_base_url}/users/{username}'
        
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Timeout:
            print('Request timed out')
        else:
            return response.json()
            
