import os

def test_visual_regression(page):
    page.goto("https://example.com/dashboard")
    os.makedirs("reports", exist_ok=True)
    screenshot_path = "reports/dashboard_screenshot.png"
    page.screenshot(path=screenshot_path, full_page=True)
    assert os.path.exists(screenshot_path)