# Integrated AI System - Kelompok AI-EL11-09

## Deskripsi Program
Repositori ini dikembangkan untuk memenuhi tugas mata kuliah **Artificial Intelligence**. Di dalam repositori ini terdapat tiga program utama berbasis Python yang mengimplementasikan **Search Algorithm**, **Expert System**, dan **Multi-Agent System**, dengan studi kasus nyata di lingkungan Kampus Telkom University dan sektor layanan kesehatan.

---

## Fitur Utama & Struktur Proyek

### 1. Search Algorithm 
* **Topik:** Navigasi Jalur Terpendek Pejalan Kaki di Kampus Telkom University.
* **Penjelasan:** Menggunakan algoritma *Uniform Cost Search (Dijkstra)* berbasis *Priority Queue* (`heapq`) untuk mencari rute tercepat dan panduan arah langkah demi langkah antar 38 titik lokasi resmi (gedung, asrama, dan gerbang kampus).

### 2. Expert System 
* **Topik:** Sistem Pakar Rekomendasi Peminatan Fakultas Teknik Elektro (FTE) Telkom University.
* **Penjelasan:** Menerapkan metode *Forward Chaining* dengan arsitektur `ElektroExpertManager` dan pertanyaan adaptif bercabang (*conditional branching*) untuk merekomendasikan program studi FTE terbaik bagi siswa SMA/SMK beserta informasi prospek kerjanya.

### 3. Multi-Agent System 
* **Topik:** Sistem Koordinasi IGD Rumah Sakit Pintar (*Smart Hospital Triage & Bed Routing*).
* **Penjelasan:** Mensimulasikan kolaborasi otonom antar-agen perangkat lunak:
  * **`HospitalAgent`:** Memantau ketersediaan kasur ICU, IGD Reguler, dan jadwal dokter spesialis secara *real-time*.
  * **`EmergencyDispatchManager`:** Menganalisis tingkat keparahan pasien (*triage*) dan mengarahkan ambulans ke rumah sakit dengan estimasi penanganan tercepat.

---

## Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python 3

---

## Cara Menjalankan Program
Jalankan masing-masing program langsung melalui terminal pada direktori proyek:

```bash
# 1. Menjalankan Search Algorithm (Navigasi Peta Kampus)
python 1_search_algorithm.py

# 2. Menjalankan Expert System (Rekomendasi Prodi FTE Tel-U)
python 2_expert_system.py

# 3. Menjalankan Multi-Agent System (Koordinasi IGD Rumah Sakit)
python 3_multi_agent_hospital.py
