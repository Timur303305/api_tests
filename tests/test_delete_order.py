import requests

class OrdersAPI:
    base_url = "https://simple-books-api.click"
    token = "f85fee8797a195a35dc2fbe87e65311868a432ed8cdf0994dd5bef6f71f3d2d9"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def delete_order(self, order_id, customer_name):
        url = f"{self.base_url}/orders/{order_id}"
        payload = {
            "customerName": customer_name
        }

        response = requests.delete(url, json=payload, headers=self.headers)
        return response

def test_delete_order():
    api = OrdersAPI()
    order_id = "aolhPf-sz8EfRHqUDTzuG"
    customer_name = "Timur"

    response = api.delete_order(order_id, customer_name)

    assert response.status_code in [200, 204], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200 and response.text.strip():
        data = response.json()
        assert data["customerName"] == customer_name
    else:
        print("Order deleted successfully (204 No Content)")