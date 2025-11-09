from dataclasses import dataclass
import requests
from faker import Faker
from pydantic import BaseModel, Field

fake = Faker()

@dataclass
class Register:
    client_name: str = None
    client_email: str = None

def generate_register_user():
    yield Register(
        client_name=fake.name(),
        client_email=fake.email()
    )

class UserRegisteredSchema(BaseModel):
    client_name: str = Field(..., alias="clientName")
    client_email: str = Field(..., alias="clientEmail")

class TestRegisterUser:
    base_url = "https://simple-books-api.click/api-clients"

    def test_generate_user(self):
        user = next(generate_register_user())
        print(f"Generated user name: {user.client_name}")
        print(f"Generated user email: {user.client_email}")

        assert user.client_name is not None
        assert user.client_email is not None

    def test_register_user(self):
        user = next(generate_register_user())

        data = UserRegisteredSchema(
            clientName=user.client_name,
            clientEmail=user.client_email
        ).model_dump(by_alias=True)

        response = requests.post(
            url=self.base_url,
            json=data
        )

        print(f"Status code: {response.status_code}")
        print(f"Response body: {response.json()}")

        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        assert "accessToken" in response.json(), "No accessToken in response"


