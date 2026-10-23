import heapq

def get_telkom_map():
    # Representasi graf lengkap 1:1 sesuai 38 titik lokasi pada peta resmi Telkom University
    return {
        "1. Telkom University Landmark Tower (TULT)": {
            "10. Research & Recreation Area": {"jarak": 200, "arah": "Berjalan ke utara menuju area riset dan rekreasi"},
            "19. Gedung Bangkit (Rektorat)": {"jarak": 350, "arah": "Turun ke selatan menuju Gedung Rektorat"}
        },
        "2. Kantin TULT": {
            "1. Telkom University Landmark Tower (TULT)": {"jarak": 80, "arah": "Berjalan menuju pelataran TULT"},
            "10. Research & Recreation Area": {"jarak": 150, "arah": "Berjalan ke area rekreasi utara"}
        },
        "3. Asrama Putra": {
            "6. Asrama Putri": {"jarak": 300, "arah": "Berjalan ke selatan menuju kompleks Asrama Putri"},
            "4. Gedung Batek (Bandung Techno Park)": {"jarak": 250, "arah": "Berjalan ke arah timur menuju BTP"}
        },
        "4. Gedung Batek (Bandung Techno Park)": {
            "3. Asrama Putra": {"jarak": 250, "arah": "Berjalan ke barat menuju Asrama Putra"},
            "10. Research & Recreation Area": {"jarak": 200, "arah": "Berjalan ke selatan menuju area riset"}
        },
        "5. Sport Center": {
            "6. Asrama Putri": {"jarak": 120, "arah": "Berjalan menuju area Asrama Putri"},
            "7. Gedung Tokong Nanas (GKU)": {"jarak": 180, "arah": "Berjalan ke arah selatan menuju Gedung Kuliah Umum"}
        },
        "6. Asrama Putri": {
            "3. Asrama Putra": {"jarak": 300, "arah": "Berjalan ke utara menuju Asrama Putra"},
            "5. Sport Center": {"jarak": 120, "arah": "Berjalan ke area Sport Center"},
            "7. Gedung Tokong Nanas (GKU)": {"jarak": 150, "arah": "Berjalan ke arah selatan menuju GKU"}
        },
        "7. Gedung Tokong Nanas (GKU)": {
            "5. Sport Center": {"jarak": 180, "arah": "Berjalan ke utara"},
            "6. Asrama Putri": {"jarak": 150, "arah": "Berjalan ke utara menuju Asrama Putri"},
            "8. Gedung Tokong Nanas / Area Parkir": {"jarak": 100, "arah": "Berjalan menyusuri area GKU"},
            "20. Gedung Damar (Auditorium)": {"jarak": 200, "arah": "Berjalan ke selatan menuju Gedung Auditorium"}
        },
        "8. Gedung Tokong Nanas (Area Pendukung)": {
            "7. Gedung Tokong Nanas (GKU)": {"jarak": 100, "arah": "Berjalan ke GKU utama"},
            "9. Gedung Lingian (Lab. Perhotelan)": {"jarak": 120, "arah": "Berjalan ke timur menuju Lab Perhotelan"}
        },
        "9. Gedung Lingian (Lab. Perhotelan)": {
            "8. Gedung Tokong Nanas (Area Pendukung)": {"jarak": 120, "arah": "Berjalan ke barat"},
            "19. Gedung Bangkit (Rektorat)": {"jarak": 180, "arah": "Berjalan ke timur menuju Rektorat"}
        },
        "10. Research & Recreation Area": {
            "1. Telkom University Landmark Tower (TULT)": {"jarak": 200, "arah": "Berjalan ke utara menuju TULT"},
            "2. Kantin TULT": {"jarak": 150, "arah": "Berjalan ke area kantin"},
            "4. Gedung Batek (Bandung Techno Park)": {"jarak": 200, "arah": "Berjalan ke utara"},
            "12. Gedung Sebatik (FIK)": {"jarak": 130, "arah": "Berjalan ke timur menuju FIK"}
        },
        "11. Gedung Benggala (TUCH)": {
            "12. Gedung Sebatik (FIK)": {"jarak": 80, "arah": "Berjalan ke timur laut"},
            "13. Gedung Miossu & Maratua (FEB)": {"jarak": 110, "arah": "Berjalan ke timur menuju FEB"}
        },
        "12. Gedung Sebatik (FIK)": {
            "10. Research & Recreation Area": {"jarak": 130, "arah": "Berjalan ke barat"},
            "11. Gedung Benggala (TUCH)": {"jarak": 80, "arah": "Berjalan ke barat daya"},
            "13. Gedung Miossu & Maratua (FEB)": {"jarak": 100, "arah": "Berjalan ke timur"}
        },
        "13. Gedung Miossu & Maratua (FEB)": {
            "11. Gedung Benggala (TUCH)": {"jarak": 110, "arah": "Berjalan ke barat"},
            "12. Gedung Sebatik (FIK)": {"jarak": 100, "arah": "Berjalan ke barat"},
            "14. Open Library": {"jarak": 90, "arah": "Berjalan ke timur menuju Open Library"}
        },
        "14. Open Library": {
            "13. Gedung Miossu & Maratua (FEB)": {"jarak": 90, "arah": "Berjalan ke barat menuju FEB"},
            "15. Kantin Dekanat": {"jarak": 60, "arah": "Berjalan ke timur laut menuju Dekanat"},
            "16. Gedung Kawalusu & Intata": {"jarak": 80, "arah": "Berjalan ke timur"},
            "19. Gedung Bangkit (Rektorat)": {"jarak": 250, "arah": "Berjalan ke barat daya menuju Rektorat"}
        },
        "15. Kantin Dekanat": {
            "14. Open Library": {"jarak": 60, "arah": "Berjalan ke barat"},
            "16. Gedung Kawalusu & Intata": {"jarak": 50, "arah": "Berjalan ke timur"}
        },
        "16. Gedung Kawalusu & Intata": {
            "14. Open Library": {"jarak": 80, "arah": "Berjalan ke barat"},
            "15. Kantin Dekanat": {"jarak": 50, "arah": "Berjalan ke barat"},
            "GATE 1": {"jarak": 100, "arah": "Berjalan keluar melalui Gate 1"}
        },
        "17. Gedung Selaru (FIT)": {
            "GATE 1": {"jarak": 150, "arah": "Berjalan ke utara menuju Gate 1"},
            "GATE 2": {"jarak": 110, "arah": "Berjalan ke timur menuju Gate 2"},
            "GATE 3": {"jarak": 120, "arah": "Berjalan ke selatan menuju Gate 3"},
            "18. Danau (Situ Techno)": {"jarak": 140, "arah": "Berjalan ke barat laut menuju Danau"}
        },
        "18. Danau (Situ Techno)": {
            "17. Gedung Selaru (FIT)": {"jarak": 140, "arah": "Berjalan ke timur"},
            "19. Gedung Bangkit (Rektorat)": {"jarak": 160, "arah": "Berjalan ke barat laut menuju Rektorat"},
            "21. Grha Wiyata Cacuk Sudarijanto": {"jarak": 130, "arah": "Berjalan ke selatan"}
        },
        "19. Gedung Bangkit (Rektorat)": {
            "1. Telkom University Landmark Tower (TULT)": {"jarak": 350, "arah": "Berjalan naik ke TULT di utara"},
            "9. Gedung Lingian (Lab. Perhotelan)": {"jarak": 180, "arah": "Berjalan ke barat"},
            "14. Open Library": {"jarak": 250, "arah": "Berjalan ke timur laut"},
            "18. Danau (Situ Techno)": {"jarak": 160, "arah": "Berjalan ke tenggara"},
            "20. Gedung Damar (Auditorium)": {"jarak": 100, "arah": "Berjalan ke barat daya"}
        },
        "20. Gedung Damar (Auditorium)": {
            "7. Gedung Tokong Nanas (GKU)": {"jarak": 200, "arah": "Berjalan ke utara"},
            "19. Gedung Bangkit (Rektorat)": {"jarak": 100, "arah": "Berjalan ke timur laut"},
            "22. Gedung Deli (Gd. P)": {"jarak": 150, "arah": "Berjalan ke barat daya"}
        },
        "21. Grha Wiyata Cacuk Sudarijanto": {
            "18. Danau (Situ Techno)": {"jarak": 130, "arah": "Berjalan ke utara"},
            "25. Gedung Penambulai (Gd. D)": {"jarak": 100, "arah": "Berjalan ke barat"},
            "26. Gedung Panehan (Pascasarjana)": {"jarak": 90, "arah": "Berjalan ke selatan"}
        },
        "22. Gedung Deli (Gd. P)": {
            "20. Gedung Damar (Auditorium)": {"jarak": 150, "arah": "Berjalan ke timur laut"},
            "23. Gedung Arakula (Gd. O)": {"jarak": 80, "arah": "Berjalan ke barat"},
            "GATE RADIO": {"jarak": 120, "arah": "Berjalan ke Gate Radio di sebelah barat"}
        },
        "23. Gedung Arakula (Gd. O)": {
            "22. Gedung Deli (Gd. P)": {"jarak": 80, "arah": "Berjalan ke timur"},
            "24. Gedung Barung (Gd. N)": {"jarak": 70, "arah": "Berjalan ke selatan"}
        },
        "24. Gedung Barung (Gd. N)": {
            "23. Gedung Arakula (Gd. O)": {"jarak": 70, "arah": "Berjalan ke utara"},
            "28. Gedung Pelampong (GSG)": {"jarak": 110, "arah": "Berjalan ke selatan"}
        },
        "25. Gedung Penambulai (Gd. D)": {
            "21. Grha Wiyata Cacuk Sudarijanto": {"jarak": 100, "arah": "Berjalan ke timur"},
            "26. Gedung Panehan (Pascasarjana)": {"jarak": 60, "arah": "Berjalan ke selatan"},
            "29. Gd. Kultubai Utara (Gd. E)": {"jarak": 90, "arah": "Berjalan ke barat"}
        },
        "26. Gedung Panehan (Pascasarjana)": {
            "21. Grha Wiyata Cacuk Sudarijanto": {"jarak": 90, "arah": "Berjalan ke utara"},
            "25. Gedung Penambulai (Gd. D)": {"jarak": 60, "arah": "Berjalan ke utara"},
            "27. Gedung Karang (Pascasarjana)": {"jarak": 70, "arah": "Berjalan ke timur"},
            "29. Gd. Kultubai Utara (Gd. E)": {"jarak": 80, "arah": "Berjalan ke barat"}
        },
        "27. Gedung Karang (Pascasarjana)": {
            "26. Gedung Panehan (Pascasarjana)": {"jarak": 70, "arah": "Berjalan ke barat"},
            "30. Gd. Kultubai Selatan (Gd. F)": {"jarak": 90, "arah": "Berjalan ke selatan"}
        },
        "28. Gedung Pelampong (GSG)": {
            "24. Gedung Barung (Gd. N)": {"jarak": 110, "arah": "Berjalan ke utara"},
            "29. Gd. Kultubai Utara (Gd. E)": {"jarak": 100, "arah": "Berjalan ke timur"},
            "31. Gedung Karaweira (Student Center)": {"jarak": 130, "arah": "Berjalan ke selatan"}
        },
        "29. Gd. Kultubai Utara (Gd. E)": {
            "25. Gedung Penambulai (Gd. D)": {"jarak": 90, "arah": "Berjalan ke timur"},
            "26. Gedung Panehan (Pascasarjana)": {"jarak": 80, "arah": "Berjalan ke timur"},
            "28. Gedung Pelampong (GSG)": {"jarak": 100, "arah": "Berjalan ke barat"},
            "30. Gd. Kultubai Selatan (Gd. F)": {"jarak": 70, "arah": "Berjalan ke selatan"}
        },
        "30. Gd. Kultubai Selatan (Gd. F)": {
            "27. Gedung Karang (Pascasarjana)": {"jarak": 90, "arah": "Berjalan ke utara"},
            "29. Gd. Kultubai Utara (Gd. E)": {"jarak": 70, "arah": "Berjalan ke utara"},
            "34. Kantin Teknik": {"jarak": 110, "arah": "Berjalan ke selatan"}
        },
        "31. Gedung Karaweira (Student Center)": {
            "28. Gedung Pelampong (GSG)": {"jarak": 130, "arah": "Berjalan ke utara"},
            "32. Lapangan Tenis": {"jarak": 50, "arah": "Berjalan ke selatan"}
        },
        "32. Lapangan Tenis": {
            "31. Gedung Karaweira (Student Center)": {"jarak": 50, "arah": "Berjalan ke utara"},
            "33. Gedung Alor": {"jarak": 80, "arah": "Berjalan ke timur"}
        },
        "33. Gedung Alor": {
            "32. Lapangan Tenis": {"jarak": 80, "arah": "Berjalan ke barat"},
            "34. Kantin Teknik": {"jarak": 90, "arah": "Berjalan ke timur"}
        },
        "34. Kantin Teknik": {
            "30. Gd. Kultubai Selatan (Gd. F)": {"jarak": 110, "arah": "Berjalan ke utara"},
            "33. Gedung Alor": {"jarak": 90, "arah": "Berjalan ke barat"},
            "35. Greenhouse": {"jarak": 70, "arah": "Berjalan ke timur"}
        },
        "35. Greenhouse": {
            "34. Kantin Teknik": {"jarak": 70, "arah": "Berjalan ke barat"},
            "36. Pool KBM": {"jarak": 80, "arah": "Berjalan ke timur"}
        },
        "36. Pool KBM": {
            "35. Greenhouse": {"jarak": 80, "arah": "Berjalan ke barat"},
            "GATE 5": {"jarak": 60, "arah": "Berjalan ke Gate 5"},
            "37. Masjid Syamsul Ulum": {"jarak": 100, "arah": "Berjalan ke timur laut"}
        },
        "37. Masjid Syamsul Ulum": {
            "36. Pool KBM": {"jarak": 100, "arah": "Berjalan ke barat daya"},
            "GATE 4": {"jarak": 70, "arah": "Berjalan ke Gate 4"},
            "GATE 3": {"jarak": 150, "arah": "Berjalan ke utara menuju Gate 3"},
            "38. Jogging Track": {"jarak": 90, "arah": "Berjalan ke timur laut"}
        },
        "38. Jogging Track": {
            "37. Masjid Syamsul Ulum": {"jarak": 90, "arah": "Berjalan ke barat daya"},
            "GATE 3": {"jarak": 110, "arah": "Berjalan ke utara menuju Gate 3"}
        },
        "GATE 1": {
            "16. Gedung Kawalusu & Intata": {"jarak": 100, "arah": "Masuk dari Gate 1 menuju area kampus"},
            "17. Gedung Selaru (FIT)": {"jarak": 150, "arah": "Berjalan ke selatan menuju FIT"}
        },
        "GATE 2": {
            "17. Gedung Selaru (FIT)": {"jarak": 110, "arah": "Berjalan ke barat menuju FIT"}
        },
        "GATE 3": {
            "17. Gedung Selaru (FIT)": {"jarak": 120, "arah": "Berjalan ke utara"},
            "37. Masjid Syamsul Ulum": {"jarak": 150, "arah": "Berjalan ke selatan menuju Masjid"},
            "38. Jogging Track": {"jarak": 110, "arah": "Berjalan ke timur"}
        },
        "GATE 4": {
            "37. Masjid Syamsul Ulum": {"jarak": 70, "arah": "Berjalan ke area masjid"}
        },
        "GATE 5": {
            "36. Pool KBM": {"jarak": 60, "arah": "Berjalan ke dalam kampus"}
        },
        "GATE RADIO": {
            "22. Gedung Deli (Gd. P)": {"jarak": 120, "arah": "Berjalan ke dalam kampus menuju Gedung Deli"}
        }
    }

def cari_rute(start, goal):
    peta = get_telkom_map()
    
    if start not in peta or goal not in peta:
        print("\n[ERROR] Lokasi tidak ditemukan di peta kampus!")
        return

    # Uniform Cost Search (Dijkstra)
    antrian = [(0, start, [start], [])]
    visited = set()

    while antrian:
        jarak, saat_ini, jalur, instruksi = heapq.heappop(antrian)
        
        if saat_ini == goal:
            print("\n" + "=" * 80)
            print(" PETUNJUK NAVIGASI JALAN KAKI KAMPUS TELKOM UNIVERSITY (1:1 LENGKAP)")
            print("=" * 80)
            print(f" Titik Asal   : {start}")
            print(f" Titik Tujuan : {goal}")
            print(f" Total Estimasi Jarak : {jarak} meter\n")
            print(" Panduan Perjalanan:")
            for i, inst in enumerate(instruksi, 1):
                print(f"   {i}. {inst}")
            print("=" * 80)
            return

        if saat_ini not in visited:
            visited.add(saat_ini)
            if saat_ini in peta:
                for tetangga, detail in peta[saat_ini].items():
                    if tetangga not in visited:
                        langkah_baru = instruksi + [f"Dari {saat_ini}: {detail['arah']} (sampai di {tetangga}, ±{detail['jarak']} meter)"]
                        heapq.heappush(antrian, (jarak + detail['jarak'], tetangga, jalur + [tetangga], langkah_baru))

    print(f"\n[INFO] Jalur pejalan kaki dari {start} ke {goal} tidak ditemukan.")

if __name__ == "__main__":
    peta = get_telkom_map()
    daftar_lokasi = list(peta.keys())

    print("=" * 80)
    print(" SISTEM NAVIGASI KAMPUS TELKOM UNIVERSITY (LENGKAP 1-38 & GATES)")
    print("=" * 80)
    print("Pilih nomor lokasi saat ini dan tujuanmu:")
    for idx, loc in enumerate(daftar_lokasi, 1):
        print(f" [{idx:2d}] {loc}")
    print("-" * 80)

    try:
        idx_start = int(input("Masukkan nomor TITIK AWAL: ")) - 1
        idx_goal = int(input("Masukkan nomor TITIK TUJUAN: ")) - 1

        if 0 <= idx_start < len(daftar_lokasi) and 0 <= idx_goal < len(daftar_lokasi):
            cari_rute(daftar_lokasi[idx_start], daftar_lokasi[idx_goal])
        else:
            print("\n[ERROR] Nomor lokasi tidak valid.")
    except ValueError:
        print("\n[ERROR] Harap masukkan angka yang benar.")
