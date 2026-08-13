import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_user_not_found():
    api_key = os.getenv("REQRES_API_KEY")
    headers = {"x-api-key": api_key}
    response = requests.get(
        "https://reqres.in/api/users/23",
        headers=headers
    )
    assert response.status_code == 404

def test_login_missing_password():
    api_key = os.getenv("REQRES_API_KEY")
    headers = {"x-api-key": api_key}
    payload = {"email": "eve.holt@reqres.in"}
    response = requests.post(
        "https://reqres.in/api/login",
        headers=headers,
        json=payload
    )
    assert response.status_code == 400