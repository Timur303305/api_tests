import requests

def test_api_auth():
    url = "https://simple-books-api.click/api-clients/"

    payload = {

       "clientName": "Postman788",
       "clientEmail": "tim404@example.com"

    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "accessToken" in data
    print(f"Access token: {data['accessToken']}")