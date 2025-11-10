import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.parametrize("username,password,should_pass", [
    ("admin", "admin123", True),
    ("wrong_user", "wrong_pass", False)
])
def test_login(page, username, password, should_pass):
    login_page = LoginPage(page)
    dashboard = DashboardPage(page)

    login_page.navigate("https://example.com/login")
    login_page.login(username, password)

    if should_pass:
        assert "Dashboard" in dashboard.get_header_text()
    else:
        assert "Invalid" in login_page.get_error_message()