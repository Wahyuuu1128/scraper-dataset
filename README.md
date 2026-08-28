# Scrapify Flow

Scrapify Flow adalah aplikasi berbasis web yang dirancang untuk mengekstraksi (scraping) data ulasan publik dari Google Play Store secara efisien. Aplikasi ini tidak hanya mengambil data mentah, tetapi juga langsung memprosesnya untuk menghasilkan visualisasi data berupa Word Cloud dan menyediakan opsi unduhan dataset. Sangat cocok digunakan oleh peneliti, analis data, maupun pengembang aplikasi untuk menganalisis umpan balik (feedback) pengguna dengan cepat.

---

## Fitur Utama

Aplikasi ini dilengkapi dengan berbagai fitur fungsional dan antarmuka yang modern:

1. **Scraping Cepat & Fleksibel**: Ekstrak ulasan langsung dari Google Play Store hanya dengan menempelkan (paste) URL aplikasi dan menentukan jumlah data yang ingin ditarik (10 hingga 5000 ulasan).
2. **Visualisasi Word Cloud Otomatis**: Secara instan membuat visualisasi "Awan Kata" dari seluruh teks ulasan pengguna untuk menemukan kata kunci atau keluhan utama yang paling sering dibicarakan.
3. **Tabel Data Interaktif**: Hasil scraping ditampilkan secara rapi dalam bentuk tabel yang responsif (mendukung scroll horizontal di perangkat mobile), mencakup kolom Rating, Nama Pengguna, Komentar, dan Tanggal.
4. **Ekspor ke CSV**: Satu klik untuk mengunduh seluruh data ulasan ke dalam format file `.csv` yang siap diolah lebih lanjut menggunakan Excel, SPSS, atau tools analisis big data lainnya.
5. **Modern UI/UX (Glassmorphism & Dark Mode)**: Antarmuka dibangun dengan gaya *Glassmorphism* yang elegan, lengkap dengan fitur pergantian tema (Light Mode & Dark Mode) yang menyimpan preferensi pengguna secara otomatis.

---

## Teknologi yang Digunakan

Scrapify Flow dibangun menggunakan kombinasi teknologi *backend* dan *frontend* modern:

### Backend
* **Python (3.10+)**: Bahasa pemrograman utama.
* **Flask**: Framework web ringan untuk mengelola *routing* dan server.
* **Google Play Scraper**: Pustaka (library) utama untuk mengekstraksi data ulasan dari API internal Play Store.
* **Pandas**: Digunakan untuk manipulasi struktur data dan mengekspor hasil ke format CSV.
* **WordCloud & Matplotlib**: Untuk memproses teks menjadi gambar visualisasi *Word Cloud* berbasis Base64.

### Frontend
* **HTML5 & CSS3**: Struktur halaman dan desain antarmuka *Glassmorphism* kustom.
* **Bootstrap 5**: Framework CSS untuk sistem *grid* dan komponen responsif.
* **FontAwesome 6**: Untuk ikon grafis vektor pada antarmuka.

### Struktur Folder 

```text
scrapify-flow/
│
├── app.py                  # File utama aplikasi (Logika Flask & Scraping)
├── hasil_ulasan.csv        # Output file dataset ulasan (dibuat otomatis)
├── README.md               # Dokumentasi proyek
│
└── templates/
    └── index.html          # Tampilan antarmuka utama (UI HTML/CSS)
