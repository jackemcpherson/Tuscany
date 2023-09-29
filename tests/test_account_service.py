from fastapi.testclient import TestClient
from account_service.main import app  # Adjust the import path accordingly

client = TestClient(app)

def test_account_crud():
    # Create account
    response = client.post("/accounts/", json={"name": "TestAccount", "balance": 0})
    assert response.status_code == 200

    # Read account
    response = client.get("/accounts/TestAccount")
    assert response.status_code == 200
    assert response.json() == {"name": "TestAccount", "balance": 0}

    # Update account
    response = client.put("/accounts/TestAccount", json={"name": "TestAccount", "balance": 50})
    assert response.status_code == 200

    # Verify update
    response = client.get("/accounts/TestAccount")
    assert response.status_code == 200
    assert response.json() == {"name": "TestAccount", "balance": 50}

    # Delete account
    response = client.delete("/accounts/TestAccount")
    assert response.status_code == 200
