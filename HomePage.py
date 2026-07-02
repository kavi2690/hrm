from playwright.sync_api import expect

class HomePage:

    def __init__(self, page):
        self.page = page

    def click_admin(self):
        self.page.locator("span:has-text('Admin')").click()

        expect(self.page).to_have_url("**/admin/**")

    def click_add(self):
        self.page.get_by_role("button", name="Add").click()