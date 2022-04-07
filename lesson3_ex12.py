import requests

class TestHeader:

    expected_header_key = "x-secret-homework-header"
    expected_header_value = "Some secret value"

    def test_check_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        headers = response.headers

        assert headers.get(self.expected_header_key) is not None, \
            f"There is no {self.expected_header_key} in {list(headers.keys())}"
        assert headers.get(self.expected_header_key) == self.expected_header_value, \
            f"Value of {self.expected_header_key} is not equal to {self.expected_header_value}"
