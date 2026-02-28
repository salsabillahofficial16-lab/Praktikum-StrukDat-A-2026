#membuat main.pyy
#buat dulu tabelnya menggunakan tabulate
from tabulate import tabulate
import kurs
import konverter
data=[
    ["USD",16875],
    ["EUR",19995],
    ["SGD",13360], 
    ["JPY",109]
    ]
print(tabulate(data, headers=["kode","kurs"],tablefmt="pretty"))

#untuk mengginput
while True:
    mata_uang_awal = input("Dari(IDR/USD/EUR/SGD/JPY):").upper()
    mata_uang_tujuan =  input("ke(IDR/USD/EUR/SGD/JPY):").upper()
    try:
        jumlah = float(input("jumlah :"))
        break
    except ValueError:
        print("Masukkan jumlah uang dengan benar!")

# mengubah mata uang ke idr  dulu
if mata_uang_awal == "USD":
    ke_idr = konverter.USD_ke_IDR(jumlah)
elif mata_uang_awal == "EUR":
    ke_idr = konverter.EUR_ke_IDR(jumlah)
elif mata_uang_awal == "SGD":
    ke_idr = konverter.SGD_ke_IDR(jumlah)
elif mata_uang_awal == "JPY":
    ke_idr = konverter.JPY_ke_IDR(jumlah)
elif mata_uang_awal == "IDR":
    ke_idr = jumlah
else:
    print("Mata uang tidak valid!!")

 #baru mengubah  idr ke mata uang 
if mata_uang_tujuan == "USD":
    hasil = konverter.IDR_ke_USD(ke_idr)
elif mata_uang_tujuan == "EUR":
    hasil = konverter.IDR_ke_EUR(ke_idr)
elif mata_uang_tujuan == "SGD":
    hasil = konverter.IDR_ke_SGD(ke_idr)
elif mata_uang_tujuan == "JPY":
    hasil = konverter.IDR_ke_JPY(ke_idr)
elif mata_uang_tujuan == "IDR":
    hasil = ke_idr
else:
    print("Mata uang tidak valid!!")

#unntuk menampilkan hasilnya  
print(f"{jumlah} {mata_uang_awal} = Rp {round(hasil,2)} {mata_uang_tujuan}")

