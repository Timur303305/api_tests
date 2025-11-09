import requests

class TestSubmitOrder:
    base_url = "https://simple-books-api.click"
    token = "f85fee8797a195a35dc2fbe87e65311868a432ed8cdf0994dd5bef6f71f3d2d9"

    def test_submit_an_order(self):
        url = f"{self.base_url}/orders"
        payload = {
            "bookId": 4,
            "customerName": "Tim"
        }
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

        data = response.json()
        assert "orderId" in data, "Response JSON does not contain 'orderId'"
        print(data)
