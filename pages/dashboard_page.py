from pages.base_page import BasePage

class DashboardPage(BasePage):
    def _init_(self, page):
        super()._init_(page)
        self.header = "h1.dashboard-title"

    def get_header_text(self):
        return self.get_text(self.header)