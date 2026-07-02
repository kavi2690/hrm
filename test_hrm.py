# import pytest
# from pages.LoginPage import LoginPage
# from pages.HomePage import HomePage
# from config import BASE_URL

# @pytest.mark.parametrize(
#     "username,password,expected",
#     [
#         ("Admin", "admin123", "Pass"),
#         ("Admin1", "admin123", "Invalid"),
#         ("Admin", "wrong123", "Invalid"),
#         ("", "admin123", "Required"),
#         ("Admin", "", "Required"),
#         ("", "", "Required")
#     ]
# )
# def test_login(page, username, password, expected):

#     login = LoginPage(page)

#     login.open(BASE_URL)
#     login.enter_username(username)
#     login.enter_password(password)
#     login.click_login()

#     if expected == "Pass":
#         login.verify_successful_login()

#     elif expected == "Invalid":
#         login.verify_invalid_credentials()

#     elif expected == "Required":
#         login.verify_required_message()
        
#     def test_admin_navigation(page):

#        login = LoginPage(page)
#        home = HomePage(page)

#        login.open(BASE_URL)
#        login.enter_username("Admin")
#        login.enter_password("admin123")
#        login.click_login()

#        login.verify_successful_login()

#        home.click_admin()

import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from config import BASE_URL


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("Admin", "admin123", "Pass"),
        ("Admin1", "admin123", "Invalid"),
        ("Admin", "wrong123", "Invalid"),
        ("", "admin123", "Required"),
        ("Admin", "", "Required"),
        ("", "", "Required")
    ]
)
def test_login(page, username, password, expected):

    login = LoginPage(page)

    login.open(BASE_URL)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    if expected == "Pass":
        login.verify_successful_login()

    elif expected == "Invalid":
        login.verify_invalid_credentials()

    elif expected == "Required":
        login.verify_required_message()


def test_admin_navigation(page):

    login = LoginPage(page)
    home = HomePage(page)

    login.open(BASE_URL)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    login.verify_successful_login()

    home.click_admin()
    home.click_add()