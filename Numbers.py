# Python Numbers
# Ada tiga tipe data numerik di Python :
# int
# float
# complex
# Variabel bertipe numerik (angka,huruf,narasi ) dibuat saat Anda menetapkan nilai pada conto berikut
x = 5    # int
y = 3.7  # float
z = 1j   # complex
# Untuk memverifikasi tipe objek apa pun di Python, gunakan type()fungsi berikut
print(type(x))
print(type(y))
print(type(z))
# Int
# Int, atau integer adalah bilangan bulat, positif atau negatif, tanpa desimal, dengan panjang tak terbatas.
# Contoh
x = 1
y = 35656222554887711.
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float
#float adalah bilangan yang mengandung 1 atau lebih angka desimal

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Angka float juga bisa berupa angka ilmiah dengan huruf "e" untuk menunjukkan pangkat 10.
x = 75e3
y = 23E4
z = -69.7e100

print(type(x))
print(type(y))
print(type(z))

# Kompleks
# ilangan kompleks ditulis dengan huruf "j" sebagai bagian imajiner
x = 4+7j
y = 9j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# Konversi Tipe
# Konversi dari satu tipe ke tipe lain:

# #convert from int to float:
x = float(6)

 #convert from float to int:
y = int(3.8)

 #convert from int to complex:
z = complex(7)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# Random Number
# Random number di Python merupakan Python tidak memiliki random()fungsi untuk membuat angka acak, tetapi Python memiliki modul bawaan randomyang dapat digunakan untuk membuat angka acak, tetapi python memiliki modul bawaan random yang dapat diguunakan membuat angkanya menjadi acak

import random

print(random.randrange(3, 17))
