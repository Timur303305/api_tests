from pprint import pprint

import requests

class BooksAPI:
    base_url = "https://simple-books-api.click"

    def get_books(self):
        url = f"{self.base_url}/books"
        response = requests.get(url)
        return response.json()

def test_get_books():
    api = BooksAPI()
    books = api.get_books()
    assert isinstance(books, list), "Expected a list of books"
    print(books)

def test_books_not_empty():
    api = BooksAPI()
    books = api.get_books()
    assert books, "The list of books is empty"
    print(books)

def test_books_have_required_fields():
    api = BooksAPI()
    books = api.get_books()
    for book in books:
        assert 'id' in book, "Book is missing 'id' field"
        assert 'name' in book, "Book is missing 'title' field"
        print(books)
