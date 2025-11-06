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

def test1():
    print()
    user = next(generate_register_user())
    print(user.client_name)
    print(user.client_email)

def test2():
    print()
    url = "https://simple-books-api.click/api-clients"
    user = next(generate_register_user())
    data = UserRegisteredSchema(
        clientName=user.client_name,
        clientEmail=user.client_email
    )
    data = data.model_dump(by_alias=True)
    response = requests.post(
        url=url,
        json=data
    )
    print(response.status_code)
    print(response.json())


