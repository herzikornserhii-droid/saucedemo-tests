import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_create_user():
    api_key = os.getenv("REQRES_API_KEY")
    headers = {"x-api-key": api_key}
    payload = {"name": "Serhii", "job": "QA Engineer"}
    response = requests.post(
         "https://reqres.in/api/users",
         headers=headers,
         json=payload
    )
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] =="Serhii"
    assert data["job"] == "QA Engineer"