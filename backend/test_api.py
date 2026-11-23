"""Cek cepat: jalankan `pytest` di dalam folder backend/.

Test memaksa mode mock agar tidak menyentuh Supabase (env dikosongkan sebelum
import; load_dotenv tidak menimpa env yang sudah ada).
"""

import os

os.environ["SUPABASE_URL"] = ""
os.environ["SUPABASE_SECRET_KEY"] = ""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["db"] == "mock"


def test_stok_filter():
    r = client.get("/stok", params={"q": "bolpoin"})
    assert r.status_code == 200
    items = r.json()["items"]
    assert len(items) == 1 and items[0]["nama"] == "Bolpoin Hitam"


def test_kategori():
    r = client.get("/kategori")
    assert r.status_code == 200
    assert "Alat Tulis" in r.json()["items"]


def test_chat_stub():
    r = client.post("/chat", json={"message": "stok pulpen?"})
    assert r.status_code == 200
    assert "stub RAG" in r.json()["reply"]
