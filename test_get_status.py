import requests

def test_get_status():
    url = "https://simple-books-api.click"
    response = requests.get(
        url=url
    )
    assert response.status_code == 200
    print(response)