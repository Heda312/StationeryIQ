// StationeryIQ — frontend skeleton (chat UI).
// Framework belum ditentukan di roadmap; dipilih HTML/CSS/JS tanpa build step.
// Ganti ke framework pilihan tim saat ditetapkan.

const API_BASE = "http://127.0.0.1:8000";

const messages = document.getElementById("messages");
const form = document.getElementById("chat-form");
const input = document.getElementById("input");
const statusEl = document.getElementById("status");
const kategoriEl = document.getElementById("kategori");

function addBubble(text, who = "bot") {
  const row = document.createElement("div");
  row.className = "row" + (who === "user" ? " row--user" : "");
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;
  row.appendChild(bubble);
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
  return row;
}

function addTyping() {
  const row = addBubble("StationeryIQ sedang mengetik…", "bot");
  row.firstChild.classList.add("bubble--typing");
  return row;
}

async function safeJson(res) {
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

async function loadStatus() {
  try {
    const data = await safeJson(await fetch(`${API_BASE}/health`));
    statusEl.textContent = data.status === "ok" ? "terhubung" : "bermasalah";
    statusEl.className = "status status--on";
  } catch {
    statusEl.textContent = "server mati";
    statusEl.className = "status status--off";
  }
}

async function loadKategori() {
  try {
    const data = await safeJson(await fetch(`${API_BASE}/kategori`));
    kategoriEl.innerHTML = "";
    for (const nama of data.items) {
      const li = document.createElement("li");
      const btn = document.createElement("button");
      btn.type = "button";
      btn.textContent = nama;
      btn.addEventListener("click", () => send(`${nama} apa saja yang tersedia?`));
      li.appendChild(btn);
      kategoriEl.appendChild(li);
    }
  } catch {
    kategoriEl.innerHTML = "<li>Gagal memuat kategori</li>";
  }
}

async function send(text) {
  const pesan = text.trim();
  if (!pesan) return;
  addBubble(pesan, "user");
  const typing = addTyping();
  try {
    const data = await safeJson(
      await fetch(`${API_BASE}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: pesan }),
      })
    );
    typing.remove();
    addBubble(data.reply ?? "(jawaban kosong)");
  } catch {
    typing.remove();
    addBubble("Maaf, sedang ada gangguan koneksi ke server. Coba lagi ya.");
  }
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const teks = input.value;
  input.value = "";
  send(teks);
});

addBubble("Halo! Saya StationeryIQ. Mau cek stok, harga, atau ukuran seragam apa hari ini?");
loadStatus();
loadKategori();
