import pytest
import json
import requests
from app.utils import test_base_url

pytestmark = pytest.mark.asyncio

base_url = test_base_url

# add_license API test
@pytest.mark.parametrize(
    "params, expected_response",
    [
        ({"certificate": "test1", "pods": 5}, {'status': True}),
        ({"certificate": "test1", "pods": 5}, {
         'error': 'Already exist', 'status': False}),
        ({"certificate": "test2", "pods": 5}, {'status': True}),
    ],
)
async def test_add_license(params, expected_response):
    requests.post(
        f"{base_url}/register",
        json={
            "email": "test3@test.com", "password": "test3"
        }
    )
    login = requests.post(
        f"{base_url}/login",
        json={
            "email": "test3@test.com", "password": "test3"
        },
    )
    token = login.json().get("auth_token")

    r = requests.post(f"{base_url}/add_license", json=params, headers={"Authorization": token})
    assert r.json() == expected_response

# register_license API test
@pytest.mark.parametrize(
    "params, expected_response",
    [
        (
            {"certificate": "test1", "cluster_id": "test_id"},
            {"pods": 5, 'status': True}
        ),
        (
            {"certificate": "test1", "cluster_id": "test_id"},
            {
                "error": "Already registered",
                "pods": 5,
                "status": False
            }
        ),
    ],
)
async def test_register_license(params, expected_response):
    r = requests.post(f"{base_url}/register_license", json=params)
    assert r.json() == expected_response


# check_license API test
@pytest.mark.parametrize(
    "params, expected_response",
    [
        (
            {"certificate": "test1", "cluster_id": "test_id"},
            {"pods": 5,
                "status": "registered"
             }
        ),
        (
            {"certificate": "test1", "cluster_id": "test_id1"},
            {
                "pods": 5,
                "status": "wrong_cluster"
            }
        ),
        (
            {"certificate": "test2", "cluster_id": ""},
            {
                "pods": 5,
                "status": "unregistered"
            }
        ),
        (
            {"certificate": "test3", "cluster_id": "test_id1"},
            {
                "pods": 0,
                "status": "doesnt_exist"
            }
        ),
    ],
)
async def test_check_license(params, expected_response):
    r = requests.get(f"{base_url}/check_license", params=params)
    assert r.json() == expected_response
