import requests

def test_single_book():
    book_id = 4
    response = requests.get(f"https://simple-books-api.click/books/{book_id}")
    print(response)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    print(data)
