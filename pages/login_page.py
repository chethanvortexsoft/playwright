from pages.base_page import BasePage

class LoginPage(BasePage):
    def _init_(self, page):
        super()._init_(page)
        self.username_field = "#username"
        self.password_field = "#password"
        self.login_button = "button[type='submit']"
        self.error_message = ".error"

    def login(self, username, password):
        self.type(self.username_field, username)
        self.type(self.password_field, password)
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)