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
            logger.info(f"Starting test: {func.__name__}")
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper


class BooksAPI:
    base_url = "https://simple-books-api.click"

    @log
    def get_books(self):
        url = f"{self.base_url}/books"
        response = requests.get(url)
        return response


@log
def test_get_books2():
    api = BooksAPI()
    response = api.get_books()

    assert response.status_code == 200, (
        f"Invalid code status, expected 200, received {response.status_code}."
    )

    logger.info("Test test_get_books2 passed successfully!")
    print(response.json())