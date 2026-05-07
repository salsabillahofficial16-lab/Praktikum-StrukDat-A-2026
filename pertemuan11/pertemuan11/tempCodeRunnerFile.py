# latihan pertemuan 11
# punya SAASAAA

  # Node (Pasien)
class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

# Queue menggunakan Linked List
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # 1. Enqueue   (nambah pasien)
    def enqueue(self, nama, keluhan):
        pasien_baru = Node(nama, keluhan)

        if self.is_empty():
            self.head = self.tail = pasien_baru
        else:
            self.tail.next = pasien_baru
            self.tail = pasien_baru

        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

    # 2. Dequeue  (panggil pasien pertama)
    def dequeue(self):
        if self.is_empty():
            print("[ERROR] Antrian kosong!")
            return None

        keluar = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {keluar.nama} (keluhan: {keluar.keluhan})")
        return keluar

    # 3. Peek / Front (lihat pasien berikutnya)
    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} — {self.head.keluhan}")

    # 4. Is Empty (cek kosong)
    def is_empty(self):
        return self._size == 0

    # 5. Size   (jumlah pasien)
    def size(self):
        return self._size

    # 6. Clear  (kosongkan antrian)
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    # Tambahan: tampilkan semua antrian
    def display(self):
        if self.is_empty():
            print("[ANTRIAN] Kosong")
            return

        print("[ANTRIAN SAAT INI]")
        current = self.head
        i = 1
        while current:
            print(f"{i}. {current.nama.upper()} → {current.keluhan}")
            current = current.next
            i += 1



# SIMULASI SESUAI SOAL
print("====================================")
print(" SISTEM ANTRIAN POLI UMUM")
print(" RS Sehat Bersama")
print("====================================\n")

antrian = Queue()

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