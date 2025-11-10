def test_ui_elements(page):
    page.goto("https://example.com/home")
    assert page.is_visible("header nav")
    assert page.is_visible("footer")
    assert page.locator("button.primary").is_enabled()