from server.app import app

def test_get_products():
    client = app.test_client()
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
