import pytest
import json
import requests
from app.utils import test_base_url

pytestmark = pytest.mark.asyncio

base_url = test_base_url

# user register API test
@pytest.mark.parametrize(
    "params, expected_response",
    [
        ({}, {"error": "Parameters can't be null"}),
        ({"email": "test1@test.com"}, {"error": "Parameters can't be null"}),
        ({"password": "test1"}, {"error": "Parameters can't be null"}),
        ({"email": "test1@testcom", "password": "test1"}, {"error": "Wrong parameter format"}),
        ({"email": "test1test.com", "password": "test1"}, {"error": "Wrong parameter format"}),
        ({"email": "test1@test.com", "password": "test1"}, {"status": True, "error": ""}),
        ({"email": "test1@test.com", "password": "test1"}, {"error": "User already exists!"})
    ],
)
async def test_register(params, expected_response):
    r = requests.post(f"{base_url}/register", json=params)
    assert r.json() == expected_response

# user login API test
@pytest.mark.parametrize(
    "params, expected_response",
    [
        ({}, {"error": "Parameters can't be null"}),
        ({"email": "test1@test.com"}, {"error": "Parameters can't be null"}),
        ({"password": "test1"}, {"error": "Parameters can't be null"}),
        ({"email": "test1@testcom", "password": "test1"}, {"error": "Wrong parameter format"}),
        ({"email": "test1test.com", "password": "test1"}, {"error": "Wrong parameter format"}),
        ({"email": "test2@test.com", "password": "test1"}, {"error": "User does not exist!"}),
        ({"email": "test1@test.com", "password": "wrong password"}, {"error": "Password is incorrect."}),
        ({"email": "test1@test.com", "password": "test1"}, {})
    ],
)
async def test_login(params, expected_response):
    r = requests.post(f"{base_url}/login", json=params)
    assert r.json().get("error") == expected_response.get("error")

# user logout API test
@pytest.mark.parametrize(
    "expected_response",
    [
        ({"status": "Logged out successfully."}),
    ],
)
async def test_logout(expected_response):
    login = requests.post(
        f"{base_url}/login",
        json={
            "email": "test1@test.com", "password": "test1"
        },
    )
    token = login.json().get("auth_token")
    r = requests.get(f"{base_url}/logout", headers={"Authorization": token})
    assert r.json() == expected_response
