# AI-EL11-09
Repositori Proyek Mata Kuliah Kecerdasan Buatan
# Integrated AI System - Kelompok EL1-09

## Deskripsi Program

Repositori ini dikembangkan untuk memenuhi tugas mata kuliah **Artificial Intelligence**. Di dalam repositori ini terdapat tiga program utama yang mengimplementasikan pilar-pilar kecerdasan buatan, yaitu **Search Algorithm**, **Expert System**, dan **Multi-Agent System**, yang dirancang khusus dengan studi kasus nyata di lingkungan **Telkom University** dan sektor kesehatan.

---

## Fitur Utama & Struktur Proyek

### 1. Search Algorithm (`1_search_algorithm.py`)
* **Topik:** Navigasi Jalur Terpendek Pejalan Kaki di Kampus Telkom University.
* **Penjelasan:** Menggunakan algoritma *Uniform Cost Search (Dijkstra)* berbasis *Priority Queue* (`heapq`) untuk mencari rute tercepat dan memberikan panduan arah langkah demi langkah (*step-by-step instructions*) di antara **38 titik lokasi resmi** (gedung perkuliahan, asrama, fasilitas umum, hingga gerbang kampus)[cite: 1].

### 2. Expert System (`2_expert_system.py`)
* **Topik:** Sistem Pakar Rekomendasi Peminatan Fakultas Teknik Elektro (FTE) Telkom University.
* **Penjelasan:** Menerapkan metode *Forward Chaining* dengan arsitektur `ElektroExpertManager`. Sistem menggunakan sistem pertanyaan bercabang adaptif (*conditional branching*) yang dirancang khusus ramah bagi siswa SMA/SMK untuk mengerucutkan pilihan ke program studi FTE yang paling pas, lengkap dengan deskripsi dan **prospek kerja** lulusannya.

### 3. Multi-Agent System (`3_multi_agent_hospital.py`)
* **Topik:** Sistem Koordinasi IGD Rumah Sakit Pintar (*Smart Hospital Triage & Bed Routing*).
* **Penjelasan:** Mensimulasikan kolaborasi otonom antar-agen perangkat lunak:
  * **`HospitalAgent`:** Setiap rumah sakit bertindak sebagai agen mandiri yang secara *real-time* memantau ketersediaan kasur ICU, IGD Reguler, serta jadwal dokter spesialis yang berjaga.
  * **`EmergencyDispatchManager`:** Menganalisis tingkat keparahan pasien (*triage*) dan berkoordinasi dengan seluruh agen rumah sakit untuk memilih rujukan terdekat dengan estimasi penanganan tercepat.

---

## Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.x
* **Library Bawaan (*Standard Library*):** `heapq`, `random`, `tkinter` (opsional)

---

## Cara Menjalankan Program

Pastikan Anda telah menginstal **Python** di komputer Anda. Anda dapat menjalankan masing-masing program langsung melalui terminal pada direktori proyek:

```bash
# 1. Menjalankan Search Algorithm (Navigasi Peta Kampus)
python 1_search_algorithm.py

# 2. Menjalankan Expert System (Rekomendasi Prodi FTE Tel-U)
python 2_expert_system.py

# 3. Menjalankan Multi-Agent System (Koordinasi IGD Rumah Sakit)
python 3_multi_agent_hospital.py
