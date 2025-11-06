import requests

def test_get_an_order():
    order_id = "aolhPf-sz8EfRHqUDTzuG"
    token = "f85fee8797a195a35dc2fbe87e65311868a432ed8cdf0994dd5bef6f71f3d2d9"

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f"https://simple-books-api.click/orders/{order_id}", headers=headers)

    assert response.status_code == 200
    data = response.json()
    print(data)
