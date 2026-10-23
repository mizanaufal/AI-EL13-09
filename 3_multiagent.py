import random

class BidderAgent:
    def __init__(self, name, max_budget, strategy):
        self.name = name
        self.max_budget = max_budget
        self.strategy = strategy  # "agresif", "hemat", atau "seimbang"
        self.active = True

    def decide_bid(self, current_price, highest_bidder):
        # Jika agen ini sudah memegang tawaran tertinggi, lewati giliran
        if highest_bidder == self.name or not self.active:
            return current_price, highest_bidder

        # Kenaikan tawaran berdasarkan strategi otonom masing-masing agen
        if self.strategy == "agresif":
            increment = random.choice([25000, 35000, 50000])
        elif self.strategy == "hemat":
            increment = random.choice([5000, 10000])
        else:  # seimbang
            increment = random.choice([15000, 20000])

        next_bid = current_price + increment

        # Cek apakah masih masuk dalam budget agen
        if next_bid <= self.max_budget:
            print(f"  + [{self.name} ({self.strategy.upper()})] menawar: Rp {next_bid:,}")
            return next_bid, self.name
        else:
            self.active = False
            print(f"  - [{self.name}] MUNDUR (Tawaran Rp {next_bid:,} melebihi budget Rp {self.max_budget:,})")
            return current_price, highest_bidder


class AuctionManager:
    def __init__(self, item_name, start_price, agents):
        self.item_name = item_name
        self.current_price = start_price
        self.agents = agents
        self.highest_bidder = None

    def run_simulation(self):
        print("\n" + "=" * 70)
        print(f" MEMULAI LELANG: {self.item_name.upper()}")
        print(f" Harga Pembuka : Rp {self.current_price:,}")
        print("=" * 70)
        
        print("\nDaftar Agen Pembeli Otonom:")
        for a in self.agents:
            print(f"  • {a.name:12s} | Strategi: {a.strategy.capitalize():8s} | Budget Max: Rp {a.max_budget:,}")
        print("-" * 70)

        round_num = 0
        while sum(1 for a in self.agents if a.active) > 1:
            round_num += 1
            print(f"\n[Putaran Lelang ke-{round_num}] (Harga Saat Ini: Rp {self.current_price:,})")
            
            for agent in self.agents:
                if sum(1 for a in self.agents if a.active) <= 1 and self.highest_bidder is not None:
                    break
                if agent.active:
                    self.current_price, self.highest_bidder = agent.decide_bid(
                        self.current_price, self.highest_bidder
                    )

        print("\n" + "=" * 70)
        print(" HASIL AKHIR SIMULASI MULTI-AGENT AUCTION")
        print("=" * 70)
        if self.highest_bidder:
            print(f" Barang Lelang   : {self.item_name}")
            print(f" Pemenang Lelang : {self.highest_bidder}")
            print(f" Harga Terjual   : Rp {self.current_price:,}")
            print(f" Total Putaran   : {round_num} Putaran")
        else:
            print(" Tidak ada agen yang sanggup menawar harga pembuka.")
        print("=" * 70)


if __name__ == "__main__":
    print("=" * 70)
    print(" SISTEM SIMULASI MULTI-AGENT E-COMMERCE AUCTION")
    print("=" * 70)
    
    nama_barang = input("Masukkan nama barang yang dilelang (contoh: Laptop Gaming): ").strip()
    if not nama_barang:
        nama_barang = "Laptop Gaming"
        
    try:
        harga_awal = int(input("Masukkan harga pembuka dalam Rupiah (contoh: 100000): "))
    except ValueError:
        harga_awal = 100000

    daftar_agen = [
        BidderAgent("Agent-Alpha", max_budget=harga_awal + 120000, strategy="agresif"),
        BidderAgent("Agent-Beta",  max_budget=harga_awal + 150000, strategy="hemat"),
        BidderAgent("Agent-Gamma", max_budget=harga_awal + 180000, strategy="seimbang"),
        BidderAgent("Agent-Delta", max_budget=harga_awal + 90000,  strategy="agresif")
    ]

    manager = AuctionManager(nama_barang, harga_awal, daftar_agen)
    manager.run_simulation()
