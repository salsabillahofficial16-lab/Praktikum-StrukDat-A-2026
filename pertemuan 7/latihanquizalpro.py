# # Input jumlah hari dan menu
# hari = int(input("Masukkan jumlah hari: "))
# menu = int(input("Masukkan jumlah menu: "))

# # Membuat matriks kosong
# data = []

# # Input data (Nested Loop)
# for i in range(hari):
#     print(f"Hari ke-{i+1}")
#     baris = []
#     for j in range(menu):
#         nilai = int(input(f"  Menu ke-{j+1}: "))
#         baris.append(nilai)
#     data.append(baris)

# # Tampilkan matriks
# print("\nData Penjualan:")
# for i in range(hari):
#     for j in range(menu):
#         print(data[i][j], end="\t")
#     print()

# # Total per hari (jumlah baris)
# print("\nTotal penjualan per hari:")
# for i in range(hari):
#     total_hari = sum(data[i])
#     print(f"Hari ke-{i+1}: {total_hari}")

# # Total per menu (jumlah kolom)
# print("\nTotal penjualan per menu:")
# for j in range(menu):
#     total_menu = 0
#     for i in range(hari):
#         total_menu += data[i][j]
#     print(f"Menu ke-{j+1}: {total_menu}")



# for i in range(2, 11, 2):
#     print(i)

# total = 25

# while True:
#     angka =  int(input("masukkan angka (0 untuk  berhenti): "))
#     data = int(input("masukkkan data  :"))
#     if angka == 0:
#         break
#     else:
#         total += angka
    
# print("total angka:", total)


# total = 0
# jumlah_data = 0

# while True:
#     angka = int(input("Masukkan angka (0 untuk berhenti): "))

#     if angka == 0:
#         break
#     else:
#         total += angka
#         jumlah_data += 1

# print("Total:", total)
# print("Jumlah data:", jumlah_data)



# total = 0
# jumlah_data = 0
# rata_rata = 0
# while True:
#     angka = int(input("Masukkan angka (0 untuk berhenti): "))

#     if angka == 0:
#         break
#     else:
#         total += angka
#         jumlah_data += 1
#         rata_rata // angka

# print("Total:", total)
# print("Jumlah data:", jumlah_data)
# print("rata_rata:", rata_rata)


# menu = {
#     1: ("roti", 4000),
#     2: ("susu", 6000)
# }

# pesanan = []
# total = 0

# while True:
#     pilih = int(input("Pilih (0 selesai): "))

#     if pilih == 0:
#         break

#     if pilih in menu:
#         jumlah = int(input("Jumlah: "))
#         pesanan.append((menu[pilih][0], jumlah, menu[pilih][1]))

# print("=== PESANAN ===")
# for item in pesanan:
#     nama, jumlah, harga = item
#     subtotal = jumlah * harga
#     total += subtotal
#     print(nama, jumlah, subtotal)

  

# print("Total:", total)




# total = 0
# jumlah_data = 0
# rata_rata = 0
# nilai_max = 0
# while True:
#     angka = int(input("Masukkan angka (-1 untuk berhenti): "))

#     if angka == -1:
#         break
#     else:
#         total += angka
#         jumlah_data += -1
# if jumlah_data == 0:
#     print("tidak ada data")
# if angka > max:
#         print("nilai maksimal")
# else:
#     rata_rata = total / jumlah_data
#     print("Total:", total)
#     print("Jumlah data:", jumlah_data)
#     print("rata_rata:", rata_rata)
#     print("nilai_terbesar", nilai_max)






# # fungsi untuk cek status kelulusan
# def cek_status(nilai):
#     if nilai >= 75:
#         return "Lulus"
#     else:
#         return "Tidak Lulus"


# # fungsi utama untuk proses data
# def proses_nilai():
#     data = []

#     jumlah = int(input("Masukkan jumlah siswa: "))

#     # loop input data
#     for i in range(jumlah):
#         print("\nData ke-", i+1)
#         nama = input("Nama: ")
#         nilai = int(input("Nilai: "))

#         # panggil fungsi lain di dalam fungsi
#         status = cek_status(nilai)

#         # simpan ke list
#         data.append([nama, nilai, status])

#     return data


# # =========================
# # program utama
# # =========================

# hasil = proses_nilai()

# print("\n=== DATA SISWA ===")
# for d in hasil:
#     print(d[0], "-", d[1], "-", d[2])



# def cek_grade(nilai):
#     if nilai >= 85:
#         return "A"
#     elif nilai >= 75:
#         return "B"
#     elif nilai >= 65:
#         return "C"
#     else:
#         return "D"

# def input_data():
#     data = []
#     jumlah = int(input("masukkan jumlah siswa: "))

#     for i in range(jumlah):
#         print("data ke", i + 1)
#         nama = input("nama: ")
#         nilai = int(input("nilai: "))
#         grade = cek_grade(nilai)
#         data.append((nama, nilai, grade))

#     return data

# hasil = input_data()

# print("==== data siswa ====")
# for nama, nilai, grade in hasil:
#     print(f"{nama}  Nilai: {nilai}  Grade: {grade}")


data = []
jumlah = int(input("masukkan  jumlah barang:"))
 

baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

if baris == 0 or kolom == 0:
    print("Matriks kosong!")
else:
    matriks = []
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            nilai = int(input(f"Masukkan elemen [{i+1},{j+1}]: "))
            baris_data.append(nilai)
        matriks.append(baris_data)
    
    b = int(input("Pilih baris elemen: "))
    k = int(input("Pilih kolom elemen: "))
    
    if 1 <= b <= baris and 1 <= k <= kolom:
        print(f"Elemen matriks[{b},{k}] = {matriks[b-1][k-1]}")
    else:
        print("Indeks diluar matriks!")


baris = int(input("Jumlah baris: "))
kolom = int(input("Jumlah kolom: "))

if baris == 0 or kolom == 0:
    print("Matriks kosong, tidak ada data")
else:
    matriks = []
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            baris_data.append(int(input(f"Elemen [{i+1},{j+1}]: ")))
        matriks.append(baris_data)
    
    total = 0
    for baris_data in matriks:
        for nilai in baris_data:
            total += nilai
    
    print("Jumlah semua elemen:", total)

# # data yang akan diurutkan

# data = [8, 5, 9, 3, 6]

# # menghitung jumlah elemen

# n = len(data)

# for i in range(n-1): # perulangan utama

# min_index = i

# # mencari nilai terkecil pada sisa array

# for j in range(i+1, n):

# if data[j] < data[min_index]:

# min_index = j

# # swap data

# temp = data[i]

# data[i] = data[min_index]

# data[min_index] = temp

# # menampilkan hasil

# print("Hasil pengurutan:", data)