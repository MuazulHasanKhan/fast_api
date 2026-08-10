from fastapi.testclient import TestClient
from app.main import app    

client = TestClient(app)

# Two functions to test the endpoint
# - test_loan_eligibility_success: tests a successful loan eligibility check
# - test_loan_eligibility_failure: tests a failed loan eligibility check

def test_loan_eligibility_pass():
    payload = {
        "income": 60000,
        "age": 25,
        "employment_status": "employed"
    }

    response = client.post("/loan_eligibility", json=payload )

    assert response.status_code == 200
    assert response.json() == {"eligible": True}

def test_loan_eligibility_fail():
    payload = {
        "income": 40000,
        "age": 20,
        "employment_status": "unemployed"
    }

    response = client.post("/loan_eligibility", json=payload)

    assert response.status_code == 200
    assert response.json() == {"eligible": False}