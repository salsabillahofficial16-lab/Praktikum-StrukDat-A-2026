def cari_buku (katalog,keyword):
 katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]
 return katalog
nomor_buku= str()
buku = []

for i in range(2):
 print(f"===mencari buku===")
 katalog  = [
  {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
 ]
 keyword = (str(input("keyword :")))
if keyword == katalog:
 print("buku yang diccari!")
elif keyword != katalog :
 print("buku  tidak ditemukan!!!")

buku = cari_buku(katalog,keyword)
