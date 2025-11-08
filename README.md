# Horus Yoga Exam 🧘‍♂️

Sebuah web app sederhana berbasis **Flask (Python)** dan **HTML/CSS/JS**, yang berfungsi untuk mengelola data pengguna dengan fitur login, registrasi, update, dan dashboard admin.

---

## 🚀 Fitur Utama
- 🔐 Registrasi dan Login User
- 👤 Dashboard untuk melihat seluruh user
- ✏️ Update dan Hapus User
- 🧩 Validasi data input
- 🧱 Database otomatis dengan Flask-Migrate

---

## 🧠 Struktur Proyek
horus-yoga-exam/
│
├── backend/
│ ├── run.py # Menjalankan Flask server
│ ├── create_db.py # Membuat database
│ ├── create_admin.py # Membuat akun admin manual
│ ├── app/
│ │ ├── config.py # Konfigurasi Flask & Database
│ │ ├── extensions.py # Inisialisasi SQLAlchemy, Migrate, Bcrypt
│ │ ├── models/
│ │ │ └── user.py # Model tabel User
│ │ ├── routes/
│ │ │ └── users.py # API endpoint untuk user
│ │ ├── services/
│ │ │ └── user_service.py# Logika bisnis user
│ │ └── utils/
│ │ └── validators.py # Validasi input user
│ └── migrations/ # File migrasi database Alembic
│
├── frontend/
│ ├── login.html # Form login
│ ├── register.html # Form registrasi
│ ├── dashboard.html # Dashboard user
│ ├── update.html # Edit data user
│ ├── css/style.css # Gaya tampilan
│ └── js/ # Logika frontend
│ ├── login.js
│ ├── register.js
│ ├── dashboard.js
│ └── update.js
│
├── requirements.txt # Library Python yang dibutuhkan
└── README.md

---

## ⚙️ Instalasi

1. **Clone / Extract Project**
   ```bash
   unzip horus-yoga-exam.zip
   cd horus-yoga-exam/backend
2. **Buat Virtual Environment & Install Dependencies**
   python -m venv venv
   source venv/bin/activate  # di Linux/macOS
   venv\Scripts\activate     # di Windows
   pip install -r requirements.txt
3. **Inisialisasi Database**
   python create_db.py
   python create_admin.py
4. **Jalankan Server**
   python run.py

🧱 Teknologi yang Digunakan
   Backend: Flask, SQLAlchemy, Alembic
   Frontend: HTML5, CSS, JavaScript
   Database: MySQL

👨‍💻 Author
   Goy Exam Project
   Project ini dibuat untuk keperluan latihan manajemen user berbasis web.