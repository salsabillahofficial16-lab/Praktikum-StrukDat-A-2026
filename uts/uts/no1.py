# # data
# pelanggan = [
#     {"id": "L001", "nama": "Ayu",  "berat": 3, "layanan": "Cuci",     "bayar": True},
#     {"id": "L002", "nama": "Bima", "berat": 5, "layanan": "Setrika",  "bayar": False},
#     {"id": "L003", "nama": "Caca", "berat": 2, "layanan": "Cuci",     "bayar": False},
#     {"id": "L004", "nama": "Doni", "berat": 4, "layanan": "Express",  "bayar": True},
# ]

# # tampilkan data
# def tampilkan_pelanggan():
#     print("=== DATA PELANGGAN ===")
    
#     i = 0
#     for p in pelanggan:
#         status = "Lunas"
#         if p["bayar"] == False:
#             status = "Belum Bayar"

#         print(i+1, p["id"], p["nama"], p["berat"], p["layanan"], status)
#         i += 1


# # filter belum bayar
# def belum_bayar():
#     hasil = []

#     for p in pelanggan:
#         if p["bayar"] == False:
#             hasil.append(p["nama"])

#     hasil.sort()

#     print("\nBelum bayar:")
#     i = 0
#     while i < len(hasil):
#         print(i+1, ".", hasil[i])
#         i += 1

#     print("Total:", len(hasil))


# tampilkan_pelanggan()
# belum_bayar()


# def info_laundry():
#     data = ("Laundry Bersih", "Jl. Mawar No. 7", "0822334455")

#     print("\nInfo Laundry:")
#     print("Nama:", data[0])
#     print("Alamat:", data[1])
#     print("Telp:", data[2])


# def rekap_layanan():
#     layanan = set()

#     # ambil unik
#     for p in pelanggan:
#         layanan.add(p["layanan"])

#     print("\nLayanan unik:", layanan)

#     # hitung
#     rekap = {}

#     for p in pelanggan:
#         l = p["layanan"]
#         if l in rekap:
#             rekap[l] = rekap[l] + 1
#         else:
#             rekap[l] = 1

#     print("Rekap:")
#     for k in rekap:
#         print(k, ":", rekap[k])

#     # cari terbanyak
#     max_nilai = max(rekap.values())

#     hasil = []
#     for k in rekap:
#         if rekap[k] == max_nilai:
#             hasil.append(k)

#     print("Terbanyak:", ", ".join(hasil))


# info_laundry()
# rekap_layanan()


# class Pelanggan:
#     jumlah = 0

#     def __init__(self, id, nama, layanan):
#         self.id = id
#         self.nama = nama
#         self.layanan = layanan
#         Pelanggan.jumlah += 1

#     def tampil(self):
#         print("ID:", self.id)
#         print("Nama:", self.nama)
#         print("Layanan:", self.layanan)

#     @staticmethod
#     def total():
#         return Pelanggan.jumlah


# class PelangganVIP(Pelanggan):
#     def __init__(self, id, nama, layanan, prioritas):
#         super().__init__(id, nama, layanan)
#         self.prioritas = prioritas

#     def tampil(self):
#         super().tampil()
#         print("Prioritas:", self.prioritas)

#         if self.prioritas == "Cepat":
#             print("** Prioritas utama **")


# p1 = Pelanggan("L001", "Ayu", "Cuci")
# p2 = PelangganVIP("L010", "Riko", "Express", "Cepat")

# p1.tampil()
# print()
# p2.tampil()

# print("\nTotal:", Pelanggan.total())



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Antrian:
#     def __init__(self):
#         self.head = None

#     def tambah(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = new_node

#     def tampil(self):
#         print("\n=== ANTRIAN ===")
#         temp = self.head
#         no = 1

#         while temp is not None:
#             d = temp.data
#             print(no, d["id"], d["nama"], d["layanan"])
#             temp = temp.next
#             no += 1

#         print("Total:", self.hitung())

#     def panggil(self):
#         if self.head is None:
#             print("Kosong")
#         else:
#             d = self.head.data
#             print("Dipanggil:", d["nama"])
#             self.head = self.head.next

#     def hapus(self, id):
#         temp = self.head
#         prev = None

#         if temp is not None and temp.data["id"] == id:
#             self.head = temp.next
#             print("Dihapus:", id)
#             return

#         while temp is not None and temp.data["id"] != id:
#             prev = temp
#             temp = temp.next

#         if temp is None:
#             print("Tidak ditemukan")
#         else:
#             prev.next = temp.next
#             print("Dihapus:", id)

#     def hitung(self):
#         count = 0
#         temp = self.head

#         while temp is not None:
#             count += 1
#             temp = temp.next

#         return count


# # contoh
# a = Antrian()
# a.tambah({"id": "L001", "nama": "Ayu", "layanan": "Cuci"})
# a.tambah({"id": "L002", "nama": "Bima", "layanan": "Setrika"})

# a.tampil()
# a.panggil()
# a.tampil()



# data pasien
pasien_hari_ini = [
    {"id": "P001", "nama": "Andi",  "usia": 34, "penyakit": "Flu",   "bayar": False},
    {"id": "P002", "nama": "Budi",  "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici",  "usia": 45, "penyakit": "Flu",   "bayar": False},
    {"id": "P004", "nama": "Dani",  "usia": 30, "penyakit": "Maag",  "bayar": True},
    {"id": "P005", "nama": "Eva",   "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag",  "bayar": False},
]

# fungsi tampilkan data pasien
def tampilkan_pasien():
    print("===== DATA PASIEN KLINIK =====")
    print("No | ID   | Nama  | Usia | Penyakit | Status")

    no = 1
    for p in pasien_hari_ini:
        if p["bayar"] == True:
            status = "Lunas"
        else:
            status = "Belum Bayar"

        print(no, "|", p["id"], "|", p["nama"], "|", p["usia"], "|", p["penyakit"], "|", status)
        no += 1


# fungsi filter pasien belum bayar
def filter_belum_bayar():
    # ambil nama pasien yang belum bayar (list comprehension)
    belum = [p["nama"] for p in pasien_hari_ini if p["bayar"] == False]

    # urutkan A-Z
    belum.sort()

    print("\n===== PASIEN BELUM BAYAR =====")
    for i in range(len(belum)):
        print(i+1, ".", belum[i])

    print("Total belum bayar:", len(belum), "pasien")


# panggil fungsi
tampilkan_pasien()
filter_belum_bayar()

# fungsi info klinik (pakai tuple)
def info_klinik():
    klinik = ("Klinik Sehat Bersama", 
              "Jl. Merdeka No. 10, Pekanbaru", 
              "0761-12345")

    print("\nInfo Klinik:")
    print("Nama   :", klinik[0])
    print("Alamat :", klinik[1])
    print("Telp   :", klinik[2])


# fungsi rekap penyakit
def rekap_penyakit():
    # ambil penyakit unik pakai set
    jenis_penyakit = set()

    for p in pasien_hari_ini:
        jenis_penyakit.add(p["penyakit"])

    print("\nJenis Penyakit Unik:", jenis_penyakit)
    print("Jumlah jenis penyakit:", len(jenis_penyakit))

    # hitung jumlah tiap penyakit pakai dictionary
    rekap = {}

    for p in pasien_hari_ini:
        penyakit = p["penyakit"]

        if penyakit in rekap:
            rekap[penyakit] += 1
        else:
            rekap[penyakit] = 1

    print("\nRekap per penyakit:")
    for k in rekap:
        print(k, ":", rekap[k], "pasien")

    # cari jumlah terbanyak
    max_jumlah = max(rekap.values())

    terbanyak = []
    for k in rekap:
        if rekap[k] == max_jumlah:
            terbanyak.append(k)

    print("Penyakit terbanyak:", ", ".join(terbanyak), f"({max_jumlah} pasien)")


# panggil fungsi
info_klinik()
rekap_penyakit()

class Pasien:
    jumlah = 0  # menghitung jumlah objek

    def __init__(self, id, nama, penyakit):
        self.__id = id
        self.__nama = nama
        self.__penyakit = penyakit
        Pasien.jumlah += 1

    # getter
    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_penyakit(self):
        return self.__penyakit

    # tampilkan info
    def tampilkan_info(self):
        print("ID      :", self.__id)
        print("Nama    :", self.__nama)
        print("Penyakit:", self.__penyakit)

    # static method
    @staticmethod
    def hitung_pasien():
        return Pasien.jumlah


# class turunan
class PasienPrioritas(Pasien):
    def __init__(self, id, nama, penyakit, prioritas):
        super().__init__(id, nama, penyakit)
        self.prioritas = prioritas

    # override
    def tampilkan_info(self):
        super().tampilkan_info()
        print("Prioritas :", self.prioritas)

        if self.prioritas == "Darurat":
            print("** Segera tangani! **")


# contoh penggunaan
p1 = Pasien("P001", "Andi", "Flu")
p2 = PasienPrioritas("P007", "Ghani", "Sesak Napas", "Darurat")

print()
p1.tampilkan_info()

print()
p2.tampilkan_info()

print("\nTotal pasien terdaftar:", Pasien.hitung_pasien())

# class node
class Node:
    def __init__(self, data):
        self.data = data   # isi data pasien (dictionary)
        self.next = None   # pointer ke node berikutnya


# class antrian pasien
class AntrianPasien:
    def __init__(self):
        self.head = None   # awal antrian

    # tambah ke belakang (FIFO)
    def tambah(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    # tampilkan semua antrian
    def tampilkan(self):
        print("\n===== ANTRIAN PASIEN =====")

        current = self.head
        no = 1

        if current is None:
            print("Antrian kosong")
            return

        while current:
            d = current.data
            print(f"[{no}] {d['id']} - {d['nama']} | {d['penyakit']}")
            current = current.next
            no += 1

        print("Total antrian:", self.hitung())

    # panggil pasien pertama (hapus depan)
    def panggil_berikutnya(self):
        if self.head is None:
            print("Antrian kosong")
            return

        print("\nMemanggil pasien berikutnya...")
        d = self.head.data
        print(f"Silakan masuk: {d['nama']} ({d['id']}) - {d['penyakit']}")

        self.head = self.head.next  # geser ke depan

    # cari berdasarkan nama
    def cari(self, nama):
        print(f"\nMencari '{nama}'...")

        current = self.head
        posisi = 1

        while current:
            if current.data["nama"] == nama:
                d = current.data
                print(f"Ditemukan: {d['id']} - {d['nama']} | {d['penyakit']} (posisi ke-{posisi})")
                return

            current = current.next
            posisi += 1

        print("Tidak ditemukan")

    # hapus berdasarkan ID
    def hapus_berdasarkan_id(self, id):
        print(f"\nMenghapus pasien dengan ID {id}...")

        current = self.head
        prev = None

        # kasus 1: di head
        if current and current.data["id"] == id:
            self.head = current.next
            print(f"{current.data['nama']} ({id}) berhasil dihapus dari antrian.")
            return

        # kasus 2: tengah / akhir
        while current and current.data["id"] != id:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
            print(f"{current.data['nama']} ({id}) berhasil dihapus dari antrian.")
        else:
            # kasus 3: tidak ditemukan
            print("ID tidak ditemukan")

    # hitung jumlah antrian
    def hitung(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


# ======================
# CONTOH PENGGUNAAN
# ======================

antrian = AntrianPasien()

antrian.tambah({"id": "P001", "nama": "Andi", "penyakit": "Flu"})
antrian.tambah({"id": "P002", "nama": "Budi", "penyakit": "Tifus"})
antrian.tambah({"id": "P003", "nama": "Cici", "penyakit": "Flu"})
antrian.tambah({"id": "P004", "nama": "Dani", "penyakit": "Maag"})

antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("P003")
antrian.tampilkan()
antrian.cari("Dani")

print("Total antrian:", antrian.hitung())

