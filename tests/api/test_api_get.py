import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_get_user_status_code():
    api_key = os.getenv("REQRES_API_KEY")
    headers = {"x-api-key": api_key}
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 200