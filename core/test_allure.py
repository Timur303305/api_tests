import requests
import allure
from test_log import log


@allure.epic("Test Allure")
class TestAllure:
    @log
    @allure.feature("Get all books")
    @allure.description("The test checks whether a list of all books is obtained")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_books(self):
        with allure.step("Getting a URL"):
            url = "https://simple-books-api.click/books"

        with allure.step("Sending a GET request"):
            response = requests.get(url=url)

        with allure.step("Validating the response status code"):
            assert response.status_code == 200, (
                f"Invalid status code: expected 200, got {response.status_code}"
            )

        with allure.step("Logging the response data"):
            data = response.json()
            allure.attach(
                str(data),
                name="Books List",
                attachment_type=allure.attachment_type.JSON
            )