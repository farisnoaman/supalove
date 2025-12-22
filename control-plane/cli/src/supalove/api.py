import requests
from typing import Optional, Dict, Any
from .config import config_manager

class APIClient:
    def __init__(self):
        self.base_url = config_manager.config.api_url.rstrip("/")
        self.session = requests.Session()

    def _get_headers(self) -> Dict[str, str]:
        headers = {"Content-Type": "application/json"}
        token = config_manager.config.access_token
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    def get(self, path: str, params: Optional[Dict] = None) -> Any:
        url = f"{self.base_url}{path}"
        resp = self.session.get(url, headers=self._get_headers(), params=params)
        return self._handle_response(resp)

    def post(self, path: str, data: Optional[Dict] = None, files: Optional[Dict] = None) -> Any:
        url = f"{self.base_url}{path}"
        if files:
            # Don't set Content-Type for multipart uploads
            headers = self._get_headers()
            headers.pop("Content-Type", None)
            resp = self.session.post(url, headers=headers, data=data, files=files)
        else:
            resp = self.session.post(url, headers=self._get_headers(), json=data)
        return self._handle_response(resp)
    
    def delete(self, path: str) -> Any:
        url = f"{self.base_url}{path}"
        resp = self.session.delete(url, headers=self._get_headers())
        return self._handle_response(resp)

    def _handle_response(self, response: requests.Response) -> Any:
        if response.status_code == 401:
            raise Exception("Unauthorized. Please run 'supalove login'.")
            
        try:
            data = response.json()
        except:
            data = {"text": response.text}

        if not response.ok:
            error_msg = data.get("detail", response.reason)
            raise Exception(f"API Error ({response.status_code}): {error_msg}")
            
        return data

api_client = APIClient()
