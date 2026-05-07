# Node untuk menyimpan data pasien
class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None


# Queue menggunakan Linked List
class AntrianPoli:
    def __init__(self):
        self.head = None
        self.tail = None
        self.jumlah = 0

    # tambah pasien
    def enqueue(self, nama, keluhan):
        pasien_baru = Node(nama, keluhan)

        if self.head is None:
            self.head = pasien_baru
            self.tail = pasien_baru
        else:
            self.tail.next = pasien_baru
            self.tail = pasien_baru

        self.jumlah += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.jumlah})")

    # panggil pasien pertama
    def dequeue(self):
        if self.head is None:
            print("[ERROR] Antrian kosong!")
            return None

        keluar = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.jumlah -= 1
        print(f"[PANGGIL] Dokter memanggil: {keluar.nama} (keluhan: {keluar.keluhan})")
        return keluar

    # lihat pasien berikutnya
    def peek(self):
        if self.head is None:
            print("[PEEK] Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} — {self.head.keluhan}")

    # cek kosong
    def is_empty(self):
        return self.head is None

    # jumlah pasien
    def size(self):
        return self.jumlah

    # kosongkan antrian
    def clear(self):
        self.head = None
        self.tail = None
        self.jumlah = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    # tampilkan semua
    def display(self):
        if self.head is None:
            print("[ANTRIAN] Kosong")
            return

        print("\n[ANTRIAN SAAT INI]")
        bantu = self.head
        no = 1

        while bantu is not None:
            print(f"{no}. {bantu.nama.upper()} → {bantu.keluhan}")
            bantu = bantu.next
            no += 1


# ================= SIMULASI =================

print("====================================")
print(" SISTEM ANTRIAN POLI UMUM")
print(" RS Sehat Bersama")
print("====================================\n")

antrian = AntrianPoli()
print("[CEK] Apakah antrian kosong?", "→ YA, antrian masih kosong." if antrian.is_empty() else "→ TIDAK")

antrian.enqueue("Budi", "demam tinggi")
antrian.enqueue("Ani", "batuk pilek")
antrian.enqueue("Citra", "sakit kepala")

print(f"\n[INFO] Jumlah pasien menunggu: {antrian.size()} orang")

antrian.peek()
antrian.dequeue()
antrian.enqueue("Dodi", "nyeri perut")
antrian.display()
antrian.dequeue()
print(f"\n[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")

antrian.clear()
print("[CEK] Apakah antrian kosong?", "→ YA, antrian sudah kosong." if antrian.is_empty() else "→ TIDAK")
print("\n====================================")
print(" Simulasi Selesai!")
print("====================================")