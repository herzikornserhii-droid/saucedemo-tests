import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_delete_user():
    api_key = os.getenv("REQRES_API_KEY")
    headers = {"x-api-key": api_key}
    response = requests.delete(
        "https://reqres.in/api/users/2",
        headers=headers
    )
    assert response.status_code ==204