import requests


class OrdersAPI:
    base_url = "https://simple-books-api.click"
    token = "f85fee8797a195a35dc2fbe87e65311868a432ed8cdf0994dd5bef6f71f3d2d9"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_all_orders(self):
        url = f"{self.base_url}/orders"
        response = requests.get(url, headers=self.headers)
        return response


def test_get_all_orders():
    api = OrdersAPI()
    response = api.get_all_orders()

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    assert isinstance(data, list), f"Expected list, got {type(data)}"

    print(data)