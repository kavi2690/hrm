from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username_txt = 'input[name="username"]'
        self.password_txt = 'input[name="password"]'
        self.login_btn = 'button[type="submit"]'

    def open(self, url):
        self.page.goto(url)

    def enter_username(self, username):
        self.page.fill(self.username_txt, username)

    def enter_password(self, password):
        self.page.fill(self.password_txt, password)

    def click_login(self):
        self.page.click(self.login_btn)

    def verify_successful_login(self):
        expect(self.page).to_have_url(
            lambda url: "dashboard" in url.lower()
        )
    def verify_successful_login(self):
     expect(
        self.page.locator("h6")
    ).to_have_text("Dashboard")

    def verify_invalid_credentials(self):
     expect(
        self.page.locator("text=Invalid credentials")
    ).to_be_visible()

    def verify_required_message(self):
     expect(
        self.page.locator("text=Required").first
    ).to_be_visible()