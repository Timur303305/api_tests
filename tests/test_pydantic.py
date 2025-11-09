import requests
import uuid
from pydantic import BaseModel, Field


class UserRegisteredSchema(BaseModel):
    clientName: str
    clientEmail: str


class TokenResponseSchema(BaseModel):
    access_token: str = Field(..., alias="accessToken")


class ClientAPI:
    base_url = "https://simple-books-api.click"

    def __init__(self):
        self.url = f"{self.base_url}/api-clients"

    def register_client(self):
        unique_id = uuid.uuid4().hex[:6]
        data = {
            "clientName": f"Wellington-{unique_id}",
            "clientEmail": f"test_{unique_id}@example.com"
        }
        response = requests.post(url=self.url, json=data)
        return response


def test_register_client_response():
    api = ClientAPI()
    response = api.register_client()

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    print(response.json())


def test_register_client_schema_validation():
    api = ClientAPI()
    response = api.register_client()

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    try:
        TokenResponseSchema.model_validate(response.json())
    except ValueError:
        raise ValueError("Invalid response body format")