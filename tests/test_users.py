import requests

BASE_URL = "https://reqres.in/api"
API_KEY = "reqres-free-v1"

HEADERS = {
    "x-api-key": API_KEY
}

def api_request(method, endpoint, **kwargs):
    """
    Helper function to make API requests with the required headers.
    
    :param method: HTTP method (e.g., 'get', 'post')
    :param endpoint: API endpoint string (e.g., '/users')
    :param kwargs: Additional arguments for requests.request
    :return: requests.Response object
    """
    url = BASE_URL + endpoint
    
    # Ensure headers include the API key, merge if other headers passed
    headers = kwargs.pop("headers", {})
    merged_headers = {**HEADERS, **headers}
    
    response = requests.request(method, url, headers=merged_headers, **kwargs)
    return response

def test_get_users_list():
    response = api_request("get", "/users?page=2")
    assert response.status_code == 200

def test_create_user():
    payload = {
        "name": "Joseph Cole",
        "job": "QA Engineer"
    }
    response = api_request("post", "/users", json=payload)
    assert response.status_code == 201

def test_user_not_found():
    """
    Test GET /users/{id} for a non-existing user returns 404.
    """
    response = api_request("get", "/users/99999")
    assert response.status_code == 404