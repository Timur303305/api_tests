import requests

def test_delete_order():
    base_url = "https://simple-books-api.click"
    order_id = "aolhPf-sz8EfRHqUDTzuG"
    token = "f85fee8797a195a35dc2fbe87e65311868a432ed8cdf0994dd5bef6f71f3d2d9"

    url = f"{base_url}/orders/{order_id}"

    payload = {
        "customerName": "Timur"
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.delete(url, json=payload, headers=headers)

    assert response.status_code in [200, 204]

    if response.status_code == 200 and response.text.strip():
        data = response.json()
        assert data["customerName"] == "Timur"
    else:
        print("Order deleted successfully (204 No Content)")