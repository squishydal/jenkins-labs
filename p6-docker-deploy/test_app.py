import pytest

from app import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_notes_start_empty(client):
    r = client.get("/api/notes")
    assert r.status_code == 200
    assert r.get_json()["notes"] == []


def test_add_note(client):
    r = client.post("/api/notes", json={"text": "built by jenkins"})
    assert r.status_code == 201
    assert r.get_json()["note"]["text"] == "built by jenkins"


def test_rejects_blank_note(client):
    r = client.post("/api/notes", json={"text": "   "})
    assert r.status_code == 400
