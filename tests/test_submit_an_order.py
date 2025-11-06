import requests

def test_submit_an_order():
    url = "https://simple-books-api.click/orders"
    token = "f85fee8797a195a35dc2fbe87e65311868a432ed8cdf0994dd5bef6f71f3d2d9"

    payload = {
        "bookId": 4,
        "customerName": "Tim"
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 201
    data = response.json()
    assert "orderId" in data
    print(data)
