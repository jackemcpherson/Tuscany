from datetime import datetime

from fastapi.testclient import TestClient

from account_service.main import app  # Adjust the import path accordingly

client = TestClient(app)


def test_account_and_transaction_crud():
    # Create account
    response = client.post(
        "/accounts/",
        json={"name": "TestAccount", "initial_balance": 0, "transactions": []},
    )
    assert response.status_code == 200

    # Read account
    response = client.get("/accounts/TestAccount")
    assert response.status_code == 200
    assert response.json() == {
        "name": "TestAccount",
        "initial_balance": 0,
        "transactions": [],
    }

    # Update account
    response = client.put(
        "/accounts/TestAccount",
        json={"name": "TestAccount", "initial_balance": 50, "transactions": []},
    )
    assert response.status_code == 200

    # Verify update
    response = client.get("/accounts/TestAccount")
    assert response.status_code == 200
    assert response.json() == {
        "name": "TestAccount",
        "initial_balance": 50,
        "transactions": [],
    }

    # Add transaction
    transaction_data = {
        "transaction_date": datetime.now().isoformat(),
        "description": "TestTransaction",
        "debit": 20,
    }
    response = client.post("/accounts/TestAccount/transactions/", json=transaction_data)
    assert response.status_code == 200

    # List transactions
    response = client.get("/accounts/TestAccount/transactions/")
    assert response.status_code == 200
    transactions = response.json()
    assert len(transactions) == 1
    assert transactions[0]["description"] == "TestTransaction"

    # Update transaction
    transaction_data = {
        "transaction_date": datetime.now().isoformat(),
        "description": "UpdatedTransaction",
        "debit": 30,
    }
    response = client.put("/accounts/TestAccount/transactions/0", json=transaction_data)
    assert response.status_code == 200

    # Delete transaction
    response = client.delete("/accounts/TestAccount/transactions/0")
    assert response.status_code == 200

    # Delete account
    response = client.delete("/accounts/TestAccount")
    assert response.status_code == 200
