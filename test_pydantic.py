import requests
import uuid
from pydantic import BaseModel, Field



class UserRegisteredSchema(BaseModel):
    clientName: str
    clientEmail: str

class TokenResponseSchema(BaseModel):
    access_token: str = Field(..., alias="accessToken")

def test1():
    url = "https://simple-books-api.click/api-clients"
    unique_id = uuid.uuid4().hex[:6]
    data = {
        "clientName": f"Wellington-{unique_id}",
        "clientEmail": f"test_{unique_id}@example.com"
    }
    response = requests.post(
        url=url,
        json=data
    )
    print(response.json())

def test2():
    url = "https://simple-books-api.click/api-clients"
    unique_id = uuid.uuid4().hex[:6]
    data = {
        "clientName": f"Wellington-{unique_id}",
        "clientEmail": f"test_{unique_id}@example.com"
    }
    response = requests.post(
        url=url,
        json=data
    )
    try:
        TokenResponseSchema.model_validate(response.json())
    except ValueError as e:
        raise ValueError("Invalid response body format")
