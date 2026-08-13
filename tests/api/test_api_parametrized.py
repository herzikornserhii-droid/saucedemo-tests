import requests
import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (2, 200),
    (3, 200),
    (23, 404),
    (999, 404),
    ])
def test_get_user_exists(user_id, expected_status):
    api_key = os.getenv("REQRES_API_KEY")
    headers = {"x-api-key": api_key}
    response = requests.get(
        f"https://reqres.in/api/users/{user_id}",
        headers=headers
    )
    assert response.status_code == expected_status