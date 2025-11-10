def test_api_call(page):
    response = page.request.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1