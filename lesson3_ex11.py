import requests

class TestCookie:
    def test_check_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookie = response.cookies

        expected_cookie_key = "HomeWork"
        expected_cookie_value = "hw_valu7e"

        for key, value in cookie.items():
            assert key == expected_cookie_key, f"Cookie_key is not equal to {expected_cookie_key}"
            assert value == expected_cookie_value, f"Cookie_value is not equal to {expected_cookie_value}"
