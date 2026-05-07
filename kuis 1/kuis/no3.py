def proses_transaksi(katalog,nama_buku,jumlah_beli):

 riwayat_transaksi= set()

buku = []

for i in range(3):
    print(f"=== transaksi pembelian ===")
    katalog= (int(input("katalog :")))
    nama_buku=(str(input("nama_buku:")))
    jumlah_beli= (int(input("jumlah_beli:")))
buku = proses_transaksi(katalog,nama_buku,jumlah_beli)