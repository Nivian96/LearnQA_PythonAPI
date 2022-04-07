import requests

class TestHeader:
    def test_check_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        headers = response.headers

        expected_header_key = "x-secret-homework-header"
        expected_header_value = "Some secret value"

        assert headers.get(expected_header_key) is not None, f"There is no {expected_header_key} in {list(headers.keys())}"
        assert headers.get(expected_header_key) == expected_header_value, f"Value of {expected_header_key} is not equal to {expected_header_value}"
