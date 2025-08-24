from app.app import app

def test_login_route():
    client = app.test_client()
    response = client.get("/login?username=admin&password=admin")
    assert response.status_code == 200
