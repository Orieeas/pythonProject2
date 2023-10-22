import pytest
from fastapi.testclient import TestClient
import httpx
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_get_employees_with_valid_email(client):
    url = "http://localhost:8000/employees"
    email = "turpis.non@Nunc.edu"

    with httpx.Client() as client:
        response = client.get(url, params={"email": email})
    assert response.status_code == 200
    employees = response.json()
    assert len(employees) == 1
    assert employees[0]["email"] == "turpis.non@Nunc.edu"


def test_get_employees_with_novalid_email(client):
    url = "http://localhost:8000/employees"
    email = "bruhbruh@Nunc.edu"

    with httpx.Client() as client:
        response = client.get(url, params={"email": email})
    assert response.status_code == 200
    employees = response.json()
    assert len(employees) == 0


def test_get_employees_without_email(client):
    url = "http://localhost:8000/employees"
    with httpx.Client() as client:
        response = client.get(url)
    assert response.status_code == 422
