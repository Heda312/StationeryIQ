# Kanban — StationeryIQ (interim)

> GitHub Projects belum dibuat (butuh akses `gh` + owner). Ini papan sementara;
> status disinkronkan manual. Lihat [`README.md`](README.md) untuk ketergantungan antar peran.

## Backlog

| ID | PIC | Periode | Prioritas | Tugas |
|---|---|---|---|---|
| TSK-FS-05 | Rafi & Rizki | Minggu 3 | Tinggi | Integrasi frontend + backend + DB + RAG (end-to-end staging) |
| TSK-FS-06 | Rafi | Minggu 3 | Tinggi | Tes E2E, validasi input ekstrem, bug fixing |
| TSK-FS-07 | Rizki | Minggu 4 | Tinggi | Deployment prototipe ke staging/production |
| TSK-FS-08 | Rafi & Rizki | Minggu 4 | Tinggi | UAT dengan pemilik toko + final fix |
| TSK-FS-09 | Rafi | Minggu 4 | Sedang | User Manual (PDF/MD + screenshot) |
| TSK-FS-10 | Rizki | Pasca-MVP | Sedang | Dashboard admin CRUD stok + transaksi + login |

## To Do (Minggu berjalan)

| ID | PIC | Prioritas | Tugas |
|---|---|---|---|
| — | Rizki | Tinggi | Kontrak JSON katalog + interface RAG (koordinasi DS & GenAI) |

## In Progress

| ID | PIC | Prioritas | Tugas | Catatan |
|---|---|---|---|---|
| TSK-FS-01 | Rafi | Sedang | Setup repo, branching, environment, **board** | repo/CI/branching ✔; board belum |
| TSK-FS-04 | Rizki | Tinggi | REST API penghubung frontend–DB | `/stok` & `/kategori` sudah baca Supabase; tinggal poles + error handling |

## Review

_(kosong)_

## Done

| ID | PIC | Periode | Deliverable |
|---|---|---|---|
| TSK-FS-02 | Rizki | Minggu 1 | Wireframe UI chat (disetujui tim) + skeleton FastAPI & frontend |
| — | — | Minggu 1 | Repo GitHub + README + aturan branching (push langsung) |
| — | — | Minggu 1 | CI dasar (lint + test) via GitHub Actions |
| — | — | Minggu 1 | Supabase tersambung (mode `supabase`) |
| — | — | Minggu 1 | Uji E2E frontend ↔ API (semua endpoint 200) |

## Cara pindah ke GitHub Projects

Butuh `gh` + akses owner. Setelah `gh auth login`:

```powershell
gh project create --owner Heda312 --title "StationeryIQ MVP Board"
# lalu tambah kartu, contoh:
gh project item-create <NUMBER> --owner Heda312 --title "TSK-FS-05 Integrasi end-to-end" --body "PIC Rafi & Rizki · Minggu 3 · Tinggi"
```
