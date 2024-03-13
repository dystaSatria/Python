from datetime import datetime, timedelta


peluncuran_roket = [
    ("Falcon 9", "2024-04-22", "ISS"),
    ("Starship", "2024-05-30", "Mars"),
    ("Artemis", "2024-06-15", "Bulan"),
    ("Falcon Heavy", "2024-07-02", "Asteroid Belt"),
]


def cari_peluncuran(tujuan):
    hasil = [peluncuran for peluncuran in peluncuran_roket if peluncuran[2].lower() == tujuan.lower()]
    if not hasil:
        print(f"Tidak ada peluncuran yang ditemukan untuk tujuan: {tujuan}")
    else:
        for peluncuran in hasil:
            print(f"Roket {peluncuran[0]} akan diluncurkan ke {peluncuran[2]} pada {peluncuran[1]}")


def hari_hingga_peluncuran_berikutnya():
    hari_ini = datetime.now()
    peluncuran_berikutnya = min(peluncuran_roket, key=lambda x: datetime.strptime(x[1], "%Y-%m-%d"))
    tanggal_peluncuran = datetime.strptime(peluncuran_berikutnya[1], "%Y-%m-%d")
    delta = tanggal_peluncuran - hari_ini
    print(f"{delta.days} hari hingga peluncuran {peluncuran_berikutnya[0]}")

def tampilkan_peluncuran():
    peluncuran_terurut = sorted(peluncuran_roket, key=lambda x: datetime.strptime(x[1], "%Y-%m-%d"))
    for peluncuran in peluncuran_terurut:
        print(f"Roket {peluncuran[0]} menuju {peluncuran[2]} pada {peluncuran[1]}")


print("Peluncuran berdasarkan tujuan (Mars):")
cari_peluncuran("Mars")
print("\nHari hingga peluncuran berikutnya:")
hari_hingga_peluncuran_berikutnya()
print("\nSemua peluncuran dalam urutan kronologis:")
tampilkan_peluncuran()
