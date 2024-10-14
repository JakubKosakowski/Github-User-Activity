import requests
from requests.exceptions import HTTPError, Timeout
from app import HTTP_ERROR, TIMEOUT_ERROR, SUCCESS
from typing import Any, NamedTuple, List, Dict

class APIResponse(NamedTuple):
    resp: List[Dict[str, Any]]
    error: int


class APIHandler():
    def __init__(self, api_base_url="https://api.github.com", token=None) -> None:
        self.api_base_url = api_base_url
        self.token = token

    def _get_headers(self) -> Dict[str, Any]:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Python-GitHubAPI"
        }
        if self.token:
            headers['Authorization'] = f"Bearer {self.token}"
        return headers
    
    def _fetch_url(self, url: str) -> APIResponse:
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
        except HTTPError:
            return APIResponse([], HTTP_ERROR)
        except Timeout:
            return APIResponse([], TIMEOUT_ERROR)
        else:
            return APIResponse(response.json(), SUCCESS)

    def get_user_info(self, username: str) -> APIResponse:
        url = f'{self.api_base_url}/users/{username}'
        return self._fetch_url(url)
        
    def get_user_events(self, username: str) -> APIResponse:
        url = f'https://api.github.com/users/{username}/events'
        return self._fetch_url(url)