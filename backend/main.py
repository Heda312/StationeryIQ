"""StationeryIQ API — skeleton FastAPI.

Endpoint minimum (roadmap): health, stok, kategori, chat.
Data masih mock. Ganti ke DB inventaris (skema path DS) dan modul RAG
(pipeline path GenAI) lewat kontrak API yang disepakati.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="StationeryIQ API", version="0.0.1")

# ponytail: origin longgar untuk dev; batasi ke URL frontend saat deploy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ponytail: data mock; ganti dengan koneksi DB inventaris (skema path DS)
STOK = [
    {"id": 1, "nama": "Bolpoin Hitam", "kategori": "Alat Tulis", "stok": 24, "harga": 3500},
    {"id": 2, "nama": "Buku Tulis 38 lembar", "kategori": "Buku & Kertas", "stok": 120, "harga": 4000},
    {"id": 3, "nama": "Seragam SD Merah Putih (M)", "kategori": "Seragam Sekolah", "stok": 8, "harga": 75000},
]
KATEGORI = ["Alat Tulis", "Buku & Kertas", "Seragam Sekolah", "Perlengkapan Lain"]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/stok")
def list_stok(q: str | None = None):
    if not q:
        return {"items": STOK}
    ql = q.lower()
    return {"items": [p for p in STOK if ql in p["nama"].lower()]}


@app.get("/kategori")
def list_kategori():
    return {"items": KATEGORI}


@app.post("/chat")
def chat(payload: dict):
    """Stub RAG. Kontrak payload respons disepakati dengan path GenAI."""
    pesan = (payload or {}).get("message", "")
    return {"reply": f"[stub RAG] Jawaban untuk: {pesan}"}
