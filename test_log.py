from functools import wraps

import requests
from loguru import logger

logger.remove()
logger.add(
    sink=r"/Users/timur/text-git-example/pythonProject1/logs.log",
    level="INFO",
    format="{time:YYYY-MM-DD} | {level} | {message}",
    rotation="10MB",
    retention="10 days"
)

def log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__} : {str(e)}")
            raise
    return wrapper

@log
def test_get_books2():
    url = "https://simple-books-api.click/books"
    response = requests.get(
        url=url
    )
    assert response.status_code == 201, f"Invalid code status, expected 200, received {response.status_code}."