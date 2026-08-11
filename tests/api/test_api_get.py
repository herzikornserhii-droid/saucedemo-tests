import requests

def test_get_user_status_code():
    headers = {"x-api-key": "free_user_3HmLPRzMqYlxe26R3wTx0QGmwCx"}
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 200