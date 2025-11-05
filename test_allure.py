import requests
import allure
from test_log import log

@allure.epic("Test allure")
class TestAllure:
    @log
    @allure.feature("Get all books")
    @allure.description("The test checks whether a list of all books is obtained")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_books2(self):
        with allure.step("Getting a URL"):
            url = "https://simple-books-api.click/books"
        with allure.step("Sending a request"):
            response = requests.get(
                url=url
        )
        with allure.step("Getting the status code and comparing it with the 200 status code"):
         assert response.status_code == 201, f"Invalid code status, expected 200, received {response.status_code}."