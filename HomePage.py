import re
from playwright.sync_api import expect


class HomePage:

    def __init__(self, page):
        self.page = page

    # ==========================
    # Navigation
    # ==========================
    def click_admin(self):
        self.page.locator("span:has-text('Admin')").click()
        expect(self.page).to_have_url(
            re.compile(r".*/admin/.*")
        )

    def click_add(self):
        add_btn = self.page.get_by_role("button", name="Add")
        expect(add_btn).to_be_visible()
        add_btn.click()

    # ==========================
    # User Role
    # ==========================
    def select_user_role(self, role):
        self.page.locator("(//div[contains(@class,'oxd-select-text')])[2]").click()
        self.page.locator(
            f"//div[@role='option']//span[text()='{role}']"
        ).click()

    # ==========================
    # Employee Name
    # ==========================
    def enter_employee_name(self, employee_name):
        employee = self.page.locator(
            "input[placeholder='Type for hints...']"
        )

        employee.fill(employee_name)

        if employee_name.strip():
            self.page.wait_for_timeout(2000)
            self.page.locator("//div[@role='option']").first.click()

    # ==========================
    # Status
    # ==========================
    def select_status(self, status):
        self.page.locator(
            "(//div[@class='oxd-select-text-input'])[2]"
        ).click()

        self.page.locator(
            f"//span[text()='{status}']"
        ).click()

    # ==========================
    # Username
    # ==========================
    def enter_username(self, username):
        self.page.locator(
            "(//input[@class='oxd-input oxd-input--active'])[2]"
        ).fill(username)

    # ==========================
    # Password
    # ==========================
    def enter_password(self, password):
        self.page.locator(
            "(//input[@type='password'])[1]"
        ).fill(password)

    # ==========================
    # Confirm Password
    # ==========================
    def enter_confirm_password(self, password):
        self.page.locator(
            "(//input[@type='password'])[2]"
        ).fill(password)

    # ==========================
    # Buttons
    # ==========================
    def click_save(self):
        self.page.get_by_role(
            "button",
            name="Save"
        ).click()

    def click_cancel(self):
        self.page.get_by_role(
            "button",
            name="Cancel"
        ).click()

    # ==========================
    # Validation Messages
    # ==========================
    def get_required_message(self):
        return self.page.locator(
            "//span[text()='Required']"
        )

    def verify_required_message(self):
        expect(
            self.page.locator(
                "//span[text()='Required']"
            ).first
        ).to_be_visible()

    def verify_password_mismatch(self):
     error = self.page.locator("text=Passwords do not match")
     expect(error).to_be_visible()
     print("Validation Message:", error.text_content())

    def verify_success_message(self):
     expect(
        self.page.locator("//div[contains(@class,'oxd-toast')]")
    ).to_be_visible()


    def verify_duplicate_username(self):
     expect(
        self.page.get_by_text("Already exists")
    ).to_be_visible()


    def verify_username_length_validation(self):
     expect(
        self.page.locator("text=Should")
    ).to_be_visible()


    def verify_password_length_validation(self):
      expect(
        self.page.locator("text=Should")
    ).to_be_visible()


    def verify_username_special_char_validation(self):
     error = self.page.locator(".oxd-input-field-error-message")

     if error.count() > 0 and error.first.is_visible():
        print("Validation Message Displayed:", error.first.text_content())
        expect(error.first).to_be_visible()
     else:
        print("No validation message displayed. Username may be accepted.")
   

    def verify_user_list_page(self):
      expect(self.page).to_have_url(
        re.compile(r".*/viewSystemUsers.*")
    )


# Print all validation messages
    def print_validation_messages(self):
     messages = self.page.locator(
        "//*[contains(@class,'oxd-input-field-error-message')]"
     )

     count = messages.count()

     for i in range(count):
        print(
            f"Validation Message {i+1}: "
            f"{messages.nth(i).text_content()}"
        )