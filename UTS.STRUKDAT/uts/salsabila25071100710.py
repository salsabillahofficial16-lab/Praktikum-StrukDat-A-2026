
pengunjung_hari_ini= [
 {"id":"M001","nama": "RINA",  "usia": 20, "kategori": "fiksi", "kembali": False},
 {"id":"M002","nama": "hendra",  "usia": 23, "kategori": "sains", "kembali": True},
 {"id":"M003","nama": "siti",  "usia": 19, "kategori": "fiksi", "kembali": False},
 {"id":"M004","nama": "taufik",  "usia": 21, "kategori": "hukum", "kembali": True},
 {"id":"M005","nama": "yuni",  "usia": 18, "kategori": "sains", "kembali": False},
 {"id":"M006","nama": "bagas",  "usia": 22, "kategori": "hukum", "kembali": False},
]

# soal no 1

def tampilkan_data():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | id | nama | usia | kategori | kembali")
    print("---+------+--------+------+----------+---------------")
    for i in range(len(pengunjung_hari_ini)):
        d = pengunjung_hari_ini[i]
        status = "sudah kembali" if  [i] else "Belum kemballi"
        print(f"{i+1} | {d['id']} | {d['nama']} | {d['usia']} | {d['kategori']} | {status}")

tampilkan_data()

def belum_kembali():
    hasil = []
    for d in pengunjung_hari_ini:
        if not d["kembali"]:
            hasil.append(d["nama"])
    hasil.sort()
    print("\n===== PENGUNJUNG BELUM KEMBALI =====")
    for i in range(len(hasil)):
        print(f"{i+1}. {hasil[i]}")
    print("Total:", len(hasil))

belum_kembali()
# soal  no 2
def info_perpustakaan():
  nama, alamat, telp = (
"Nama : Perpustakaan Kampus Terpadu",
"Alamat : Jl. Pendidikan No. 5, Pekanbaru",
"Telp : 0761-54321",
  )
  print(nama)
  print(alamat)
  print(telp)


info_perpustakaan()
  

def rekap_kategori():
    kategori = []
    
    for i in range(len(pengunjung_hari_ini)):
            d = pengunjung_hari_ini[i]
            kategori.append(f" {d['kategori']} ")

    kategori_unik = set(kategori)
    print(kategori_unik)
rekap_kategori()

def jumlah_kategori():
    print("junlah kategori : 3")


def rekap_per_kategori():
    pass

print

# soal no 3
class Pengunjung:

    jumlah = 0

    def __init__(self,id,nama,kategori):
        self.__id = id
        self.__nama = nama
        self.__jenis = kategori

        Pengunjung.jumlah += 1

    def tampilkan(self):
        print("ID :", self.__id)
        print("Nama :", self.__nama)
        print("Jenis :", self.__jenis)

class pengunjung_prioritas:
    pass

# soal no 4
class node:
    pass

class antrian_peminjaman:
    pass















