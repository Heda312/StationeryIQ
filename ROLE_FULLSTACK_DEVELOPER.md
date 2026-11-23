# Konteks Role: Full Stack Developer — StationeryIQ (Toko Anugerah)

> File ini menjelaskan siapa user, apa tugasnya, dan bagaimana ia terhubung dengan anggota tim lain.
> Sumber: *Roadmap & Task Breakdown per Path — StationeryIQ Toko Anugerah* (sheet "Roadmap Proyek" dan "Task Tracker Tim").
> Status tugas adalah snapshot dari spreadsheet dan bisa sudah berubah. Verifikasi ke repo/task board sebelum mengandalkannya.

---

## 1. Peran user

- **Path:** Full Stack Developer (FSD). Path ini diisi 2 orang: **Rafi** dan **Rizki**.
- **Nama user:** `<isi: Rafi / Rizki>`
- **Tanggung jawab inti:** membangun dan mengirimkan aplikasi web yang dipakai pengguna akhir. Cakupannya frontend chat UI, backend REST API (FastAPI), koneksi ke database inventaris, integrasi modul RAG buatan path GenAI, deployment, UAT, dan user manual.
- **Bukan tanggung jawab user (milik path lain):**
  - Path Data Scientist (Hasya, Intan): data, skema database, evaluasi akurasi stok.
  - Path GenAI Engineer (Ghally, Wahyu): pipeline RAG, vector store, prompt, guardrails.
  - Agent boleh membantu memahami atau menyambungkan hasil kerja path lain, tetapi tidak mengubah wilayah mereka tanpa diminta.

## 2. Tentang proyek

| Item | Isi |
|---|---|
| Nama | **StationeryIQ**: Retail Copilot Chatbot untuk **Toko Anugerah** |
| Domain | Toko fisik ATK (alat tulis kantor) dan seragam sekolah |
| Tujuan MVP | Chatbot yang menjawab pertanyaan stok, harga, dan ukuran/varian seragam dalam bahasa sehari-hari |
| Durasi MVP | 4 minggu: **20 Nov – 20 Des 2026** |
| Tim | 6 orang (3 path × 2 orang), proyek capstone |
| Milestone akhir | **Live demo & UAT dengan pemilik toko, 20 Des 2026** |
| Fokus pasca-MVP | Demand forecasting dan dashboard admin CRUD |
| Pengguna akhir | Pemilik toko, kasir, dan staf. **Non-teknis**, jadi UI harus sederhana dan ramah |

**Arsitektur tiga pilar:** Web Client (frontend) ↔ API Backend (FastAPI) ↔ RAG Engine (modul GenAI) dengan Database inventaris di belakangnya. Pekerjaan inti FSD adalah menyatukan semuanya.

## 3. Stack dan keputusan teknis yang sudah tertulis

- Backend: **FastAPI** (Python), dengan router async untuk memanggil retrieval RAG.
- Database: relasional, **PostgreSQL atau SQLite** (skema dirancang path DS, FSD memakai ORM/DB client untuk terhubung).
- Frontend: aplikasi web dengan chat UI. Framework **belum disebut** di roadmap.
- Desain: wireframe di Figma atau mock UI, font **Montserrat & Roboto**.
- Repo: GitHub. **Commit langsung ke `main` diperbolehkan** (branch protection tidak aktif); branch + PR opsional untuk perubahan besar/berisiko. Project board (kanban) dan CI/CD dasar.
- Endpoint minimum: chat, stok, kategori, health check.
- Error handling standar (404, 500) dengan pesan yang rapi.
- Respons RAG bisa streaming atau non-streaming. Payload harus disepakati dengan path GenAI.

## 4. Task FSD (dari Task Tracker)

| ID | PIC | Periode | Prioritas | Status* | Tugas | Deliverable | Indikator keberhasilan |
|---|---|---|---|---|---|---|---|
| TSK-FS-01 | Rafi | Minggu 1 | Sedang | sedang berjalan | Setup repo GitHub, aturan branching, environment, board tugas | Repo terkonfigurasi + Kanban aktif | Seluruh tim terhubung ke repo dan board teratur |
| TSK-FS-02 | Rizki | Minggu 1 | Tinggi | sedang berjalan | Wireframe UI chat non-teknis + inisialisasi skeleton FastAPI & frontend | Wireframe Figma/mock UI + template source code | Desain disetujui tim, kerangka backend-frontend berjalan |
| TSK-FS-03 | Rafi | Minggu 2 | Tinggi | Sedang Berjalan | UI chat interaktif (input box, riwayat chat, loading state) | Komponen UI chat web, responsif | Lancar dan responsif di browser HP & desktop. Ada indikator animasi mengetik |
| TSK-FS-04 | Rizki | Minggu 2 | Tinggi | Sedang Berjalan | Endpoint REST API penghubung frontend ke database inventaris | Routes (stok, kategori, health check) + DB connector | Endpoint membaca DB produk dengan HTTP 200. Error handling 404/500 terpasang |
| TSK-FS-05 | Rafi & Rizki | Minggu 3 | Tinggi | Belum Mulai | Integrasi Frontend + Backend API + Database + pipeline RAG | Web app terintegrasi end-to-end (staging) | Kueri dari chat UI memicu RAG dan jawaban tampil di web |
| TSK-FS-06 | Rafi | Minggu 3 | Tinggi | Belum Mulai | Tes end-to-end, validasi input kosong/karakter acak, bug fixing | Test suite E2E + changelog bug fix | Aplikasi tidak crash pada input ekstrem atau kueri beruntun. Validasi form ketat |
| TSK-FS-07 | Rizki | Minggu 4 | Tinggi | Belum Mulai | Deployment prototipe ke server staging/production untuk demo | Web app aktif di production URL | Bisa diakses stabil lewat link tanpa error runtime. Siapkan cadangan offline/lokal jika koneksi toko bermasalah |
| TSK-FS-08 | Rafi & Rizki | Minggu 4 | Tinggi | Belum Mulai | UAT interaktif dengan pemilik toko + final bug fixes | Berita acara UAT + rilis MVP v1.0 | Pemilik toko berhasil menguji pengecekan stok langsung. Minor UI fix selesai dalam 1×24 jam pasca demo |
| TSK-FS-09 | Rafi | Minggu 4 | Sedang | Belum Mulai | Menyusun User Manual aplikasi | Dokumen User Manual (PDF/MD, brosur ringkas) | Mudah dipraktikkan pemilik/kasir. Dilengkapi screenshot langkah demi langkah |
| TSK-FS-10 | Rizki | Pasca-MVP | Sedang | Belum Mulai | Dashboard web admin CRUD stok mandiri + pencatatan transaksi | Modul admin (CRUD produk, restock, riwayat transaksi) | Pemilik toko menambah/mengedit produk tanpa developer. Ada autentikasi login khusus pemilik |

\* Snapshot spreadsheet: 2 selesai, 2 sedang berjalan, 6 belum mulai.

## 5. Timeline dan milestone

| Fase | Periode | Milestone FSD | Kriteria checkpoint (seluruh tim) |
|---|---|---|---|
| Minggu 1 | 20–27 Nov | **M1**: skeleton backend/frontend berjalan, repo + CI/CD dasar, wireframe disepakati | Katalog data terstandar + prompt template + skeleton app berjalan |
| Minggu 2 | 28 Nov–5 Des | **M2**: chat UI + REST API siap menerima modul RAG | Database aktif + engine RAG lokal berfungsi + UI chat interaktif |
| Minggu 3 | 6–13 Des | **M3**: aplikasi terintegrasi penuh, tanpa blocker error fatal | Aplikasi end-to-end staging-ready + log akurasi >95% |
| Minggu 4 | 14–20 Des | **M4**: live di production, UAT disetujui, user manual diserahkan | StationeryIQ v1.0 deployed + User Manual + Data Dictionary + Video Demo |
| Pasca-MVP | Bulan ke-2+ | **V2.0**: platform terpadu (chat customer + dashboard admin + modul transaksi) | StationeryIQ V2.0: Full Retail Copilot & Inventory Intelligence Platform |

## 6. Titik sambung dengan path lain

Hal yang FSD harus sepakati atau sediakan, atau yang FSD terima dari path lain:

| Fase | Dengan | Isi sambungan |
|---|---|---|
| M1 | DS | Sepakati **format JSON data katalog** yang dikonsumsi frontend dan endpoint API |
| M1 | GenAI | Tentukan **spesifikasi interface modul RAG** (input prompt → respons LLM). Selaraskan payload respons streaming/non-streaming |
| M1 | DS | DS memberi masukan kebutuhan **filter kategori produk** di UI |
| M2 | DS | Hubungkan **ORM/DB client** FastAPI ke skema database buatan DS. DS ikut menguji kelengkapan atribut di **kartu informasi produk** |
| M2 | GenAI | Siapkan **router API async** untuk memanggil retrieval RAG. GenAI menyesuaikan output markdown RAG ke format pesan UI chat |
| M3 | DS | Pastikan **logging kueri** tersimpan rapi untuk evaluasi akurasi. DS memverifikasi stok yang tampil di layar sama dengan tabel database |
| M3 | GenAI | Sesuaikan **timeout handling dan streaming response**. GenAI menguji kestabilan koneksi socket/REST pada kueri beruntun |
| M4 | DS | Masukkan panduan format data ke **lampiran teknis User Manual** |
| M4 | GenAI | Pastikan **parameter model RAG** hasil fine-tuning stabil di environment deploy. GenAI memantau kuota token API dan latensi di server demo |
| Pasca | DS | Siapkan **endpoint data analitik** untuk grafik tren di dashboard admin |
| Pasca | GenAI | Integrasikan fitur laporan AI berkala dengan **notifikasi terjadwal** di web. Perbarui vector store otomatis saat produk baru diinput di web |

## 7. Target dan batasan yang memengaruhi kode FSD

- **Akurasi stok adalah segalanya.** Chatbot tidak boleh menyatakan barang ada jika stok riil 0 (zero false-positive). UI harus menampilkan data stok persis sesuai database dan tidak mengarang atau membulatkan.
- **Latensi:** target respons RAG di bawah 2.5 detik. Timeout, loading state, dan streaming di FSD harus mengakomodasi ini. Query SQL pencarian atribut ditargetkan di bawah 50 ms.
- **Responsif:** roadmap menyebut desktop dan tablet, tracker menyebut HP dan desktop. Anggap ketiganya harus berfungsi.
- **Ketahanan:** aplikasi tidak boleh crash pada input kosong, karakter acak, atau kueri beruntun. Sediakan cadangan offline/lokal untuk demo.
- **Kemudahan operasional:** pemilik toko harus bisa menjalankan aplikasi di browser "tanpa setup rumit" dan mengoperasikannya mandiri setelah demo.
- **Bahasa:** antarmuka dan pesan error dalam Bahasa Indonesia yang ramah. Chatbot memakai istilah lokal toko, misalnya pulpen = bolpoin = pena dan baju SD = seragam merah putih.
- **Cakupan chatbot:** hanya ATK dan seragam. Pertanyaan di luar itu ditolak sopan oleh guardrails (urusan GenAI), dan UI tidak boleh merusak perilaku itu.
- **Pasca-MVP:** area admin wajib terproteksi autentikasi (login khusus pemilik toko).

## 8. Aturan kerja untuk AI agent (default, silakan edit)

1. Bantu user sebagai Full Stack Developer: frontend, FastAPI, integrasi DB, integrasi RAG lewat kontrak API, deployment, testing, dan dokumentasi (user manual).
2. **Periksa repo dan kode yang ada terlebih dahulu.** Jangan mengasumsikan framework frontend, hosting, atau pilihan database yang belum tertulis di sini. Tanyakan jika tidak jelas.
3. Hormati kontrak antar path (bagian 6). Jika perlu mengubah format JSON atau payload yang dipakai path lain, sebutkan dampaknya dan sarankan koordinasi dengan PIC terkait.
4. Utamakan kesederhanaan dan keandalan di atas fitur. Target utama adalah **live demo yang stabil pada 20 Des 2026**.
5. Ikuti aturan Git tim: **commit langsung ke `main` diperbolehkan** (branch protection tidak aktif). Sebelum push: `git pull --ff-only`. CI (lint + test) wajib hijau. Gunakan branch + PR untuk perubahan besar/berisiko atau saat butuh review.
6. Prioritaskan task berstatus **Tinggi** dan yang dekat dengan checkpoint milestone.
7. Beri tahu user jika permintaan menyentuh wilayah path DS atau GenAI.
8. Gunakan Bahasa Indonesia saat berkomunikasi dengan user, kecuali diminta lain. Nama kode, komentar, dan commit mengikuti konvensi repo.

## 9. Perlu dilengkapi user

- [ ] Nama user (Rafi / Rizki)
- [ ] URL repo GitHub dan struktur folder
- [ ] Framework frontend yang dipakai
- [ ] Database yang dipilih (PostgreSQL / SQLite) dan tempat hosting/deploy
- [ ] Konvensi kode, commit, dan branch tim
- [ ] Status terbaru task FS-03 dan FS-04
