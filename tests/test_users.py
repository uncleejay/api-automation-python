# tests/test_users.py

import requests

# Base URL for the API
BASE_URL = "https://reqres.in/api"

def test_get_users_list():
    """
    Test the GET /users endpoint returns a valid user list.
    """
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200

    json_data = response.json()
    assert "data" in json_data
    assert isinstance(json_data["data"], list)
    assert all("email" in user for user in json_data["data"])