def info# ==============================
# DATA AWAL
# ==============================
data_laptop = [
{"id":"L001","nama":"Andi","kelas":"TI1","jenis":"Gaming","kembali":False},
{"id":"L002","nama":"Budi","kelas":"TI2","jenis":"Office","kembali":True},
{"id":"L003","nama":"Citra","kelas":"TI1","jenis":"Design","kembali":False},
{"id":"L004","nama":"Dina","kelas":"TI3","jenis":"Gaming","kembali":True},
{"id":"L005","nama":"Eka","kelas":"TI2","jenis":"Office","kembali":False},
{"id":"L006","nama":"Fajar","kelas":"TI1","jenis":"Design","kembali":False}
]

# ==============================
# SOAL 1
# ==============================
def tampilkan_data():
    print("===== DATA PEMINJAM LAPTOP =====")
    print("No | ID | Nama | Kelas | Jenis | Status")

    for i in range(len(data_laptop)):
        d = data_laptop[i]

        status = "Sudah" if d["kembali"] else "Belum"

        print(f"{i+1} | {d['id']} | {d['nama']} | {d['kelas']} | {d['jenis']} | {status}")


def belum_kembali():
    hasil = []

    for d in data_laptop:
        if not d["kembali"]:
            hasil.append(d["nama"])

    hasil.sort()

    print("\n===== BELUM KEMBALI =====")
    for i in range(len(hasil)):
        print(f"{i+1}. {hasil[i]}")

    print("Total:", len(hasil))


# ==============================
# SOAL 2
# ==============================
def info_lab():
    lab = (
        "Lab Komputer Kampus",
        "Gedung A Lantai 2",
        "0761-11111"
    )

    print("\nInfo Lab:")
    print("Nama :", lab[0])
    print("Alamat :", lab[1])
    print("Telp :", lab[2])


def rekap_jenis():
    unik = {d["jenis"] for d in data_laptop}

    print("\nJenis laptop unik:", unik)
    print("Jumlah jenis:", len(unik))

    rekap = {}

    for d in data_laptop:
        j = d["jenis"]
        rekap[j] = rekap.get(j,0) + 1

    print("\nRekap jenis:")
    for k,v in rekap.items():
        print(k,":",v,"peminjam")

    maks = max(rekap.values())

    terbanyak = []
    for k in rekap:
        if rekap[k] == maks:
            terbanyak.append(k)

    print("\nJenis terbanyak:", ", ".join(terbanyak), f"({maks} peminjam)")


# ==============================
# SOAL 3 OOP
# ==============================
class Peminjam:

    jumlah = 0

    def __init__(self,id,nama,jenis):
        self.__id = id
        self.__nama = nama
        self.__jenis = jenis

        Peminjam.jumlah += 1

    def tampilkan(self):
        print("ID :", self.__id)
        print("Nama :", self.__nama)
        print("Jenis :", self.__jenis)

    @staticmethod
    def total():
        return Peminjam.jumlah


class PeminjamPrioritas(Peminjam):

    def __init__(self,id,nama,jenis,prioritas):
        super().__init__(id,nama,jenis)
        self.prioritas = prioritas

    def tampilkan(self):
        super().tampilkan()
        print("Prioritas :", self.prioritas)

        if self.prioritas == "Tinggi":
            print("** Dahulukan **")


# ==============================
# SOAL 4 LINKED LIST
# ==============================
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class AntrianLaptop:

    def __init__(self):
        self.head = None


    def tambah(self,data):
        baru = Node(data)

        if self.head == None:
            self.head = baru
            return

        bantu = self.head
        while bantu.next != None:
            bantu = bantu.next

        bantu.next = baru


    def tampilkan(self):
        print("\n===== ANTRIAN LAPTOP =====")

        bantu = self.head
        no = 1

        while bantu != None:
            d = bantu.data
            print("["+str(no)+"]", d["id"], "-", d["nama"], "|", d["jenis"])
            bantu = bantu.next
            no += 1

        print("Total:", self.hitung())


    def panggil(self):

        if self.head == None:
            print("Antrian kosong")
            return

        data = self.head.data
        self.head = self.head.next

        print("Dipanggil:", data["nama"])


    def cari(self,nama):

        bantu = self.head
        pos = 1

        while bantu:
            if bantu.data["nama"] == nama:
                print("Ditemukan posisi",pos)
                return

            bantu = bantu.next
            pos += 1

        print("Tidak ditemukan")


    def hitung(self):

        bantu = self.head
        j = 0

        while bantu:
            j += 1
            bantu = bantu.next

        return j


# ==============================
# MAIN
# ==============================
tampilkan_data()
belum_kembali()

info_lab()
rekap_jenis()

print("\n===== OOP =====")
p1 = Peminjam("L001","Andi","Gaming")
p1.tampilkan()

print()

p2 = PeminjamPrioritas("L007","Gilang","Office","Tinggi")
p2.tampilkan()

print("Total objek:", Peminjam.total())


antrian = AntrianLaptop()

antrian.tambah({"id":"L001","nama":"Andi","jenis":"Gaming"})
antrian.tambah({"id":"L002","nama":"Budi","jenis":"Office"})
antrian.tambah({"id":"L003","nama":"Citra","jenis":"Design"})
antrian.tambah({"id":"L004","nama":"Dina","jenis":"Gaming"})

antrian.tampilkan()
antrian.panggil()
antrian.tampilkan()

antrian.cari("Dina")
print("Total antrian:", antrian.hitung())









    for i in range(len(pengunjung_hari_ini)):
        d = pengunjung_hari_ini[i]

        status = "Sudah" if d["kembali"] else "Belum"

        print(f"{i+1} | {d['id']} | {d['nama']} | {d['kelas']} | {d['jenis']} | {status}")


def belum_kembali():
    hasil = []

    for d in pengunjung_hari_ini:
        if not d["kembali"]:
            hasil.append(d["nama"])

    hasil.sort()

    print("\n===== BELUM KEMBALI =====")
    for i in range(len(hasil)):
        print(f"{i+1}. {hasil[i]}")

    print("Total:", len(hasil))

