import sys

from fastapi.testclient import TestClient

sys.path.append("..")

from user_service.main import app  # Adjust the import path accordingly

client = TestClient(app)


def test_user_crud():
    # Step 1: Create user
    payload = {"username": "TestUser", "email": "Test@User.com"}
    response = client.post("/users/", json=payload)
    assert response.status_code == 200
    user_id = response.json()["user_id"]
    assert user_id is not None

    # Step 2: Retrieve and check user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == payload

    # Step 3: Update user
    updated_payload = {"username": "TestUser", "email": "User@Test.com"}
    response = client.put(f"/users/{user_id}", json=updated_payload)
    assert response.status_code == 200

    # Step 4: Retrieve and check updated user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == updated_payload

    # Step 5: Delete user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200

    # Verify user has been deleted
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() is None
