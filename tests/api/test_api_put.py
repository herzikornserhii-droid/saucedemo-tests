import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_update_user():
    api_key = os.getenv("REQRES_API_KEY")
    headers = {"x-api-key": api_key}
    payload = {"name": "Serhii", "job": "Senior QA Engineer"}
    response = requests.put(
        "https://reqres.in/api/users/2",
        headers=headers,
        json=payload
    )
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == "Senior QA Engineer"