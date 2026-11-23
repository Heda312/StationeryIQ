"""Cek cepat: jalankan `pytest` di dalam folder backend/."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_stok_filter():
    r = client.get("/stok", params={"q": "bolpoin"})
    assert r.status_code == 200
    items = r.json()["items"]
    assert len(items) == 1 and items[0]["nama"] == "Bolpoin Hitam"


def test_chat_stub():
    r = client.post("/chat", json={"message": "stok pulpen?"})
    assert r.status_code == 200
    assert "stub RAG" in r.json()["reply"]
