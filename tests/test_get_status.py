import requests


class BooksAPI:
    base_url = "https://simple-books-api.click"

    def get_status(self):
        response = requests.get(self.base_url)
        return response


def test_get_status():
    api = BooksAPI()
    response = api.get_status()

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print(response)