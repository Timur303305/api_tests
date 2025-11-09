import requests

class TestApiAuth:
    base_url = "https://simple-books-api.click/api-clients/"

    def test_api_auth(self):
        payload = {
            "clientName": "Postman788",
            "clientEmail": "tim404@example.com"
        }

        response = requests.post(self.base_url, json=payload)

        assert response.status_code == 201, (
            f"Expected status code 201, but got {response.status_code}"
        )

        data = response.json()

        assert "accessToken" in data, "Response does not contain 'accessToken'"

        print(f"Access token: {data['accessToken']}")