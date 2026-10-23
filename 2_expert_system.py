Berikut adalah pembaruan kode `2_expert_system.py` menggunakan **sistem pertanyaan bercabang (*adaptive/conditional branching*)**.

Dengan metode ini, pertanyaan kedua akan **menyesuaikan secara otomatis** berdasarkan kategori besar yang dipilih pengguna pada pertanyaan pertama, sehingga prosesnya jauh lebih interaktif dan mengerucut langsung ke 1 pilihan program studi terbaik lengkap dengan deskripsi dan prospek kerjanya:

```python
class ElektroExpertManager:
    def __init__(self):
        # Database deskripsi dan prospek kerja prodi FTE Telkom University
        self.details = {
            "S1 Teknik Telekomunikasi": {
                "deskripsi": "Fokus pada jaringan internet, Wi-Fi, sinyal seluler, dan komunikasi nirkabel.",
                "prospek": "Network Engineer, Telecommunication Specialist, 5G/RF Engineer, ISP/Operator Seluler (Telkom, Indosat, Telkomsel)."
            },
            "S1 Teknik Elektro": {
                "deskripsi": "Fokus pada instalasi kelistrikan arus kuat, sistem tenaga, dan mesin listrik.",
                "prospek": "Electrical Engineer, Power Plant Engineer, PLN, Industri Manufaktur & Otomasi Kelistrikan."
            },
            "S1 Teknik Komputer": {
                "deskripsi": "Fokus pada rakit PC, pemrograman (coding), sistem tertanam (embedded), dan IoT.",
                "prospek": "Software Engineer, Embedded Systems Developer, IoT Engineer, Full-Stack Developer."
            },
            "S1 Teknik Fisika": {
                "deskripsi": "Fokus pada instrumentasi industri, sensor pintar, sistem kendali, dan otomasi.",
                "prospek": "Instrumentation & Control Engineer, Automation Specialist, Quality Control Engineer di industri besar."
            },
            "S1 Teknik Biomedis": {
                "deskripsi": "Fokus pada rekayasa teknologi kesehatan dan perancangan alat medis digital.",
                "prospek": "Clinical Engineer, Biomedical Equipment Technician, R&D Medical Device, Industri Rumah Sakit & Alat Kesehatan."
            },
            "S1 Teknik Sistem Energi": {
                "deskripsi": "Fokus pada pengembangan energi terbarukan, panel surya, dan efisiensi energi hijau.",
                "prospek": "Renewable Energy Consultant, Solar Power Engineer, Energy Auditor, Perusahaan Energi Hijau & BUMN."
            }
        }
        self.rekomendasi = []

    def run(self):
        print("=" * 65)
        print(" SISTEM PAKAR REKOMENDASI PEMINATAN FAKULTAS TEKNIK ELEKTRO")
        print("=" * 65)
        print("Jawablah pertanyaan berikut dengan mengetik nomor pilihanmu.\n")
        
        # Pertanyaan Utama (Cabang 1)
        print("Q1: Bidang utama apa yang paling menarik perhatianmu?")
        print("  1. Komputer, Coding, & Jaringan Internet (Digital/Software)")
        print("  2. Kelistrikan Rumah, Mesin, & Sumber Energi (Power/Hardware)")
        print("  3. Robotika, Sensor Otomatis, & Alat Kesehatan (Device/System)")
        
        pilih1 = input("\nPilihanmu (1/2/3): ").strip()
        
        # Pertanyaan Menyesuaikan Berdasarkan Jawaban Q1
        if pilih1 == '1':
            print("\n[MANAGER] Mengarahkan ke rumpun Digital & Software...")
            print("Q2: Apa yang lebih ingin kamu pelajari lebih dalam?")
            print("  1. Cara merakit PC, belajar pemrograman (coding), dan perangkat IoT.")
            print("  2. Cara kerja jaringan internet, Wi-Fi, dan sinyal seluler/5G.")
            
            pilih2 = input("\nPilihanmu (1/2): ").strip()
            if pilih2 == '1':
                self.rekomendasi.append("S1 Teknik Komputer")
            else:
                self.rekomendasi.append("S1 Teknik Telekomunikasi")
                
        elif pilih1 == '2':
            print("\n[MANAGER] Mengarahkan ke rumpun Power & Hardware...")
            print("Q2: Apa yang lebih menarik bagimu?")
            print("  1. Instalasi kelistrikan, arus kuat, dan mesin-mesin listrik.")
            print("  2. Pengembangan energi terbarukan, panel surya, dan energi hijau.")
            
            pilih2 = input("\nPilihanmu (1/2): ").strip()
            if pilih2 == '1':
                self.rekomendasi.append("S1 Teknik Elektro")
            else:
                self.rekomendasi.append("S1 Teknik Sistem Energi")
                
        elif pilih1 == '3':
            print("\n[MANAGER] Mengarahkan ke rumpun Device & System...")
            print("Q2: Mana fokus teknologi yang ingin kamu kembangkan?")
            print("  1. Membuat sistem sensor otomatis, kontrol industri, atau robot.")
            print("  2. Menciptakan teknologi alat kesehatan atau perangkat medis digital.")
            
            pilih2 = input("\nPilihanmu (1/2): ").strip()
            if pilih2 == '1':
                self.rekomendasi.append("S1 Teknik Fisika")
            else:
                self.rekomendasi.append("S1 Teknik Biomedis")
        else:
            # Fallback jika input tidak valid
            self.rekomendasi.append("S1 Teknik Elektro")

        self.display_result()

    def display_result(self):
        print("\n" + "=" * 65)
        print(" HASIL REKOMENDASI UTAMA (PALING SESUAI)")
        print("=" * 65)
        for prodi in self.rekomendasi:
            info = self.details[prodi]
            print(f"\n  • Program Studi : {prodi}")
            print(f"    Deskripsi     : {info['deskripsi']}")
            print(f"    Prospek Kerja : {info['prospek']}")
        print("=" * 65)

if __name__ == "__main__":
    manager = ElektroExpertManager()
    manager.run()

```
