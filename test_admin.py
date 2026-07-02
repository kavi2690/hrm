
import random
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from config import BASE_URL


def test_add_user_all_scenarios(page):

    login = LoginPage(page)
    home = HomePage(page)

    # Login
    login.open(BASE_URL)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    login.verify_successful_login()

    home.click_admin()

    # ==================================================
    # 1. Empty Fields Validation
    # ==================================================
    home.click_add()
    home.click_save()
    home.verify_required_message()

    # ==================================================
    # 2. Password Mismatch Validation
    # ==================================================
    home.click_cancel()
    home.click_add()

    home.select_user_role("Admin")
    home.enter_employee_name("b")
    home.select_status("Enabled")
    home.enter_username(f"user{random.randint(1000,9999)}")
    home.enter_password("Admin@123")
    home.enter_confirm_password("Admin@321")
    home.click_save()

    home.verify_password_mismatch()

    # ==================================================
    # 3. Duplicate Username Validation
    # ==================================================
    home.click_cancel()
    home.click_add()

    home.select_user_role("Admin")
    home.enter_employee_name("a")
    home.select_status("Enabled")
    home.enter_username("Admin")
    home.enter_password("Admin@123")
    home.enter_confirm_password("Admin@123")
    home.click_save()

    home.verify_duplicate_username()

    # ==================================================
    # 4. Username Too Short
    # ==================================================
    home.click_cancel()
    home.click_add()

    home.select_user_role("Admin")
    home.enter_employee_name("m")
    home.select_status("Enabled")
    home.enter_username("a")
    home.enter_password("Admin@123")
    home.enter_confirm_password("Admin@123")
    home.click_save()

    home.verify_username_length_validation()

    # ==================================================
    # 5. Username Too Long
    # ==================================================
    home.click_cancel()
    home.click_add()

    long_username = "a" * 50

    home.select_user_role("Admin")
    home.enter_employee_name("a")
    home.select_status("Disabled")
    home.enter_username(long_username)
    home.enter_password("Admin@123")
    home.enter_confirm_password("Admin@123")
    home.click_save()

    home.verify_username_length_validation()

    # ==================================================
    # 6. Password Minimum Length
    # ==================================================
    home.click_cancel()
    home.click_add()

    home.select_user_role("Admin")
    home.enter_employee_name("b")
    home.select_status("Enabled")
    home.enter_username(f"user{random.randint(1000,9999)}")
    home.enter_password("12385")
    home.enter_confirm_password("12385")
    home.click_save()

    home.verify_password_length_validation()

    # ==================================================
    # 7. Special Characters Username
    # ==================================================
    home.click_cancel()
    home.click_add()

    home.select_user_role("Admin")
    home.enter_employee_name("c")
    home.select_status("Disabled")
    home.enter_username("@@@###*")
    home.enter_password("Admin@123")
    home.enter_confirm_password("Admin@123")
    home.click_save()

    home.verify_username_special_char_validation()

    # ==================================================
    # 8. Cancel Button Functionality
    # ==================================================
    home.click_cancel()
    home.verify_user_list_page()

    # ==================================================
    # 9. Positive Test Case
    # ==================================================
    home.click_add()

    home.select_user_role("Admin")
    home.enter_employee_name("d")
    home.select_status("Enabled")
    

    username = f"testuser{random.randint(10000,99999)}"

    home.enter_username(username)
    home.enter_password("Admin@123")
    home.enter_confirm_password("Admin@123")
    home.click_save()

    home.verify_success_message()
    home.print_validation_messages()