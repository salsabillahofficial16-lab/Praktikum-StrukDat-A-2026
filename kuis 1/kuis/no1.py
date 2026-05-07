def tambah_buku(Nama,harga,stok):

 daftar_buku ={
  ["masukkan nama buku :"],
  ["masukkkan harga buku :"],
  ["masukkan stok buku :"]
}
 return daftar_buku
harga = int ()
stok = int ()

for i in range(3):
 print(f"====daftar buku====")
 Nama = (str(input("Nama :")))
 harga = (int(input("harga :")))
 stok = (int(input("stok :")))
if harga <= 0:
 print("eror")



buku= tambah_buku(Nama,harga,stok)







