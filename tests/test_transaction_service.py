from fastapi.testclient import TestClient

from transaction_service.main import app

client = TestClient(app)


def test_transaction_service():
    # 1. Create a transaction
    response = client.post(
        "/transactions/",
        json={"from_account": "Account1", "to_account": "Account2", "amount": 100.0},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "transaction added", "transaction_id": 0}

    # 2. Retrieve this transaction
    response = client.get("/transactions/0")
    assert response.status_code == 200
    assert response.json() == {
        "from_account": "Account1",
        "to_account": "Account2",
        "amount": 100.0,
    }
