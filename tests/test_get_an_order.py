import requests


class OrdersAPI:
    base_url = "https://simple-books-api.click"
    token = "f85fee8797a195a35dc2fbe87e65311868a432ed8cdf0994dd5bef6f71f3d2d9"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_order(self, order_id):
        url = f"{self.base_url}/orders/{order_id}"
        response = requests.get(url, headers=self.headers)
        return response


def test_get_an_order():
    api = OrdersAPI()
    order_id = "aolhPf-sz8EfRHqUDTzuG"

    response = api.get_order(order_id)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    print(data)






