import pytest
import requests

BASE = "https://jsonplaceholder.typicode.com"


@pytest.mark.api
def test_get_post():
    r = requests.get(f"{BASE}/posts/1", timeout=10)
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert "title" in body


@pytest.mark.api
def test_create_post():
    r = requests.post(f"{BASE}/posts", json={"title": "qa", "body": "demo", "userId": 1}, timeout=10)
    assert r.status_code == 201
    assert r.json()["title"] == "qa"


@pytest.mark.api
def test_response_time_under_2s():
    r = requests.get(f"{BASE}/posts", timeout=10)
    assert r.elapsed.total_seconds() < 2
