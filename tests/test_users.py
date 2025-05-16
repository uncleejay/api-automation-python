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

def test_create_user():
    """
    Test the POST /users endpoint creates a new user.
    """
    payload = {
        "name": "Joseph Cole",
        "job": "QA Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201

    json_data = response.json()
    assert json_data["name"] == payload["name"]
    assert json_data["job"] == payload["job"]

def test_user_not_found():
    """
    Test GET /users/{id} for a non-existing user returns 404.
    """
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404