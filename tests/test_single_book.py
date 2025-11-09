import requests

class TestSingleBook:
    base_url = "https://simple-books-api.click/books"

    def test_single_book(self):
        book_id = 4
        response = requests.get(f"{self.base_url}/{book_id}")
        print(response)
        assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

        data = response.json()
        assert data["id"] == book_id, f"Expected book id {book_id}, got {data['id']}"
        print(data)
