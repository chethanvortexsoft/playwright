class BasePage:
    def _init_(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def get_text(self, selector):
        return self.page.inner_text(selector)

    def click(self, selector):
        self.page.click(selector)

    def type(self, selector, text):
        self.page.fill(selector, text)