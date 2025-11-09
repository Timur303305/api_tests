import requests

class TestUpdateOrder:
    base_url = "https://simple-books-api.click"
    token = "f85fee8797a195a35dc2fbe87e65311868a432ed8cdf0994dd5bef6f71f3d2d9"

    def test_update_order(self):
        order_id = "aolhPf-sz8EfRHqUDTzuG"
        url = f"{self.base_url}/orders/{order_id}"

        payload = {
            "customerName": "Timur"
        }
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        response = requests.patch(url, json=payload, headers=headers)

        assert response.status_code in [200, 204], (
            f"Unexpected status code: {response.status_code}"
        )

        if response.status_code == 200 and response.text.strip():
            data = response.json()
            assert data["customerName"] == "Timur", (
                f"Expected customerName='Timur', got '{data.get('customerName')}'"
            )
        else:
            print("Order updated successfully (204 No Content)")



