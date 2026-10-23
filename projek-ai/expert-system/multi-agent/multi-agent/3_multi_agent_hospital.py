class HospitalAgent:
    def __init__(self, name, distance_km, icu_beds, regular_beds, specialists):
        self.name = name
        self.distance_km = distance_km
        self.icu_beds = icu_beds
        self.regular_beds = regular_beds
        self.specialists = specialists

    def evaluate_patient(self, severity, needed_specialist):
        # cek kasur sesuai tingkat keparahan
        if severity == "kritis" and self.icu_beds <= 0:
            return False, 999, "DITOLAK (Kamar ICU Penuh)"
        if severity == "sedang" and self.regular_beds <= 0:
            return False, 999, "DITOLAK (Kasur IGD Reguler Penuh)"

        # cek dokter spesialis
        has_specialist = needed_specialist in self.specialists
        if severity == "kritis" and not has_specialist:
            return False, 999, f"DITOLAK (Dokter Spesialis {needed_specialist.capitalize()} Tidak Tersedia)"

        # estimasi waktu penanganan
        est_time = self.distance_km * 2
        if not has_specialist:
            est_time += 15

        status_msg = f"SIAP MENERIMA (Estimasi Penanganan: {est_time} menit)"
        return True, est_time, status_msg

    def admit_patient(self, severity):
        if severity == "kritis":
            self.icu_beds -= 1
        else:
            self.regular_beds -= 1


class EmergencyDispatchManager:
    def __init__(self, hospitals):
        self.hospitals = hospitals

    def route_patient(self, patient_name, severity, needed_specialist):
        print("\n" + "-" * 72)
        print(f" [SINYAL DARURAT] Pasien: {patient_name} | Status: {severity.upper()} | Butuh: Spesialis {needed_specialist.capitalize()}")
        print("-" * 72)
        print(" [MANAGER] Menghubungi seluruh Agen Rumah Sakit terdekat...")

        candidates = []
        for hospital in self.hospitals:
            accepted, est_time, reason = hospital.evaluate_patient(severity, needed_specialist)
            print(f"  -> [{hospital.name:20s}] ({hospital.distance_km} km) : {reason}")
            if accepted:
                candidates.append((est_time, hospital))

        if candidates:
            candidates.sort(key=lambda x: x[0])
            best_time, best_hospital = candidates[0]
            best_hospital.admit_patient(severity)
            print(f"\n [KEPUTUSAN MULTI-AGENT] Ambulans diarahkan ke => {best_hospital.name}")
            print(f"  • Alasan Pemilihan : Waktu respons tercepat ({best_time} menit) & fasilitas siap.")
        else:
            print("\n [PERINGATAN KRITIS] Semua RS terdekat penuh/tidak memenuhi syarat! Mengaktifkan rujukan regional.")

    def show_hospital_status(self):
        print("\n" + "=" * 72)
        print(" STATUS KAPASITAS REAL-TIME AGEN RUMAH SAKIT")
        print("=" * 72)
        for h in self.hospitals:
            spesialis_str = ", ".join([s.capitalize() for s in h.specialists])
            print(f" • {h.name:20s} | Jarak: {h.distance_km:2d} km | ICU: {h.icu_beds} | IGD: {h.regular_beds} | Dokter: {spesialis_str}")
        print("=" * 72)


if __name__ == "__main__":
    rs_agents = [
        HospitalAgent("RS Telkom Medika", distance_km=2, icu_beds=0, regular_beds=3, specialists=["umum", "paru"]),
        HospitalAgent("RS Santosa Bandung", distance_km=6, icu_beds=2, regular_beds=5, specialists=["jantung", "saraf", "bedah"]),
        HospitalAgent("RS Al-Islam", distance_km=5, icu_beds=1, regular_beds=2, specialists=["jantung", "paru", "anak"]),
        HospitalAgent("RS Hasan Sadikin", distance_km=9, icu_beds=4, regular_beds=8, specialists=["jantung", "saraf", "bedah", "paru"])
    ]

    manager = EmergencyDispatchManager(rs_agents)

    # langsung minta input dulu
    nama = input("1. Masukkan nama/kode pasien : ").strip() or "Pasien-01"
    kondisi = input("2. Tingkat keparahan (kritis / sedang) : ").strip().lower()
    if kondisi not in ["kritis", "sedang"]:
        kondisi = "kritis"
    dokter = input("3. Kebutuhan spesialis (jantung / saraf / bedah / paru) : ").strip().lower()
    if not dokter:
        dokter = "jantung"

    # baru cari RS yang cocok
    manager.route_patient(nama, severity=kondisi, needed_specialist=dokter)
    manager.show_hospital_status()
