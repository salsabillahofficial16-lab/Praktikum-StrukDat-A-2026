#lattihan 13 
# class HashTable
class HashTable:
    # =========================================
    # Sistem penyimpanan data buku perpustakaan
    # =========================================
    def __init__(self):
        self.kode = 10
        self.table = [[] for _ in range(self.kode)]

    # =========================================
    # Hash Function
    # Mengubah kode buku menjadi index bucket
    # =========================================
    def hash_function(self, kode):
        total = 0

        # Menjumlahkan Unicode tiap karakter
        for char in str(kode):
            total += ord(char)

        return total % self.kode

    # =========================================
    # Insert Function
    # Menambahkan pasangan kode:judul
    #
    # Jika kode sudah ada:
    # -> update judul
    #
    # Jika kode belum ada:
    # -> append ke bucket
    # =========================================
    def insert(self, kode, judul):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == kode:
                bucket[i] = (kode, judul)
                print(f"Data dengan kode '{kode}' berhasil di-update")
                return
        # Jika kode belum ada
        # Tambahkan data baru ke bucket
        bucket.append((kode, judul))
        print(f"Data '{kode}:{judul}' berhasil ditambahkan")

    # =========================================
    # Get Function
    # Mengambil value berdasarkan kode
    #
    # Return:
    # - value jika ditemukan
    # - None jika tidak ditemukan
    # =========================================
    def get(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for k, v in bucket:
            if k == kode:
                return v
        # Jika tidak ditemukan
        return None

    # =========================================
    # Delete Function
    # Menghapus data berdasarkan kode
    #
    # Return:
    # - True jika berhasil
    # - False jika gagal
    # =========================================
    def delete(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == kode:
                # Hapus data
                del bucket[i]
                print(f"Data dengan kode '{kode}' berhasil dihapus")
                return True

        # Jika kode tidak ditemukan
        print(f"Kode '{kode}' tidak ditemukan!")
        return False

    # =========================================
    # Display Function
    # Menampilkan seluruh isi hash table
    # =========================================
    def display(self):

        print("\n===== PENIMPANAN DATA BUKU DI PERPUSTAKAAN =====")

        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")

        print("===================================================\n")


# =========================================
# PROGRAM UTAMA
# =========================================

# Membuat object hash table
data_buku = HashTable()

# Insert data
print("==== insert data buku ====")
data_buku.insert("BK111", "Mahir C++ Dalam Satu Jam")
data_buku.insert("BK222", "Python Dasar")
data_buku.insert("BK333", "Matematika Diskrit")
data_buku.insert("BK444", "Atomic Habits")
data_buku.insert("BK555", "Sapiens: A Brief History of Humankind")
data_buku.insert("BK666", "The Power of Habit")
data_buku.insert("BK777", "Clean Code")
data_buku.insert("BK888", "The Pragmatic Programmer")
print("===============================================") #biar rapi ajaaa

# Menampilkan isi hash table
data_buku.display()

# Menambahkan kode yang hasil hash-nya sama
print(" ==== masukkan  data berikut: ====")
data_buku.insert("BK045", "Mein kampf")
data_buku.insert("BK111", "Bumi Manusia")
print("=================================")
# Tampilkan hash table
data_buku.display()

# Mengambil data berdasarkan kode
print("==== mencari data buku ====")
print("masukkan kode buku:", data_buku.get("BK111"))
print("masukkan kode buku:", data_buku.get("BK222"))
print("======================================")

# Update data
print("==== update data buku ====")
data_buku.insert("BK222", "Buku B Baru")
# Menampilkan isi terbaru
data_buku.display()

# Mencari data yang tidak ada
print("==== mencari data yang tidak ada ====")
print("masukkan kode buku:", data_buku.get("BK999")) #cari buku berdasarkan kode yang tidak ada dalam hash table
print("======================================")

# Menghapus data
print("==== menghapus data buku ====")
data_buku.delete("BK111")
# Menampilkan isi setelah delete
data_buku.display()
