"""Akses data StationeryIQ ke Supabase.

Env kosong -> mode mock (dipakai CI dan dev tanpa kredensial).
Schema produk bisa berubah: baris dikirim apa adanya (`select *`) supaya
perubahan kolom tidak menuntut perubahan kode; nama tabel dapat diatur lewat
env `PRODUCTS_TABLE`.
"""

import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()

PRODUCTS_TABLE = os.getenv("PRODUCTS_TABLE", "products")

# ponytail: data mock; hanya dipakai bila env Supabase kosong
MOCK_STOK = [
    {"id": 1, "nama": "Bolpoin Hitam", "kategori": "Alat Tulis", "stok": 24, "harga": 3500},
    {"id": 2, "nama": "Buku Tulis 38 lembar", "kategori": "Buku & Kertas", "stok": 120, "harga": 4000},
    {"id": 3, "nama": "Seragam SD Merah Putih (M)", "kategori": "Seragam Sekolah", "stok": 8, "harga": 75000},
]
MOCK_KATEGORI = ["Alat Tulis", "Buku & Kertas", "Seragam Sekolah", "Perlengkapan Lain"]


@lru_cache
def _client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SECRET_KEY") or os.getenv("SUPABASE_KEY")
    if not (url and key):
        return None
    from supabase import create_client

    return create_client(url, key)


def mode() -> str:
    """\"supabase\" bila kredensial terpasang, selain itu \"mock\"."""
    return "supabase" if _client() else "mock"


def _match(rows, q):
    if not q:
        return rows
    ql = q.lower()
    return [r for r in rows if ql in str(r.get("nama", "")).lower()]


def fetch_stok(q: str | None = None):
    c = _client()
    if c is None:
        return _match(MOCK_STOK, q)
    rows = c.table(PRODUCTS_TABLE).select("*").execute().data
    return _match(rows, q)


def fetch_kategori():
    c = _client()
    if c is None:
        return MOCK_KATEGORI
    rows = c.table(PRODUCTS_TABLE).select("kategori").execute().data
    out = []
    for r in rows:
        k = r.get("kategori")
        if k and k not in out:
            out.append(k)
    return out
