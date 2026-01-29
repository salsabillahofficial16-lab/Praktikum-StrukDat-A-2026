#Python Strings
#string dalam python dikelilingi tanda kutip tunggal atau ganda
print("Haii")
print('Haii')
#Quotes Inside Quotes
#nggunakan tanda kutip di dalam sebuah string, asalkan tanda kutip tersebut tidak sama dengan tanda kutip yang mengelilingi string tersebut 
print("masakan padang")
print("dia panggil aku 'Do kyungso'")
print('aku manggil dia "chanyoel"')
#Menetapkan String ke Variabel
#tujuannya memasukkan nilai stringg ke subuah variabel dengan memasukkan nama variabel diikuti dengan tanda = dan string tersebut
f = "pak somad jualan tomat"
print(f)

#String Multibaris
#contoh
E = """Belajar terasa lebih ringan dan semangat ketika mendengarkan lagu exo."""
print(E)
#atau bisa juga dengan 3 tanda kutip tunggal
s = '''Belajar terasa lebih ringan, dan semangat ketika mendengarkan, lagu exo.'''
print(s)

#String adalah Array
#Contoh
i = "welcome, exo!"
print(i[3]) #ini artinya mengambil angka ke3 didalam string tersebut

#Melakukan perulangan melalui sebuah string
for t in "back it up":
  print(t) #ini artinya melakukan perulangan huruf 

#String Length
y = "hai aku exol"
print(len(y))

#Check String
txt = "Tommorrow X Together is a famous k-pop in korea!"
print("k-pop" in txt)

#Check if NOT
txt = "Tommorrow X Together is a famous k-pop in korea!"
print("good" not in txt) #kebalikannya contoh check string 

#Slicing
j = "nama saya, salsa"
print(j[11:13])#hitungnya mulai dari nol dulu

#Slice From the Start
m = "mahasiswa angkatan 25"
print(m[:9])#memasukkan huruf sesuai dengan banyak angka yang ditentukan

#Slice To the End
p = "mahasiswa angkatan 25!"
print(p[2:])

#Negative Indexing
y = "mahasiswa angkatan 25!"
print(y[-7:-3])

#Upper Case
v = "aku suka musik"
print(v.upper()) #mengubah hurufnya menjadi besar

#Lower Case
q = "AKU SUKA MUSIK"
print(q.lower())#kebalikan dari upper case

#Remove Whitespace
l = "          AKU SUKA MUSIK      "
print(l.strip()) # menghapus spasi dan tab

#Replace String
a = "AKU SUKA MUSIK "
print(a.replace("K", "J"))

#Split String
a = "pacu jalur, adalah budaya, kabupaten kuansing"
print(a.split(","''))#memisahkan sebuah string menjadi beberapa bagian sesuai dengan perintahya

#String Concatenation
g = "budaya di"
e = "indonesia"
c = g + e
print(c)

#F-Strings
age = 18
txt = f"My name is salsa, I am {age}"
print(txt)

#Placeholders and Modifiers
price = 100
txt = f"harganya sekitar {price} Ribu Rupiah"
print(txt)

