#mengubah mata uang yang berbeda ke idr
import kurs

def USD_ke_IDR(jumlah) :
    jumlah = jumlah * kurs.kurses['USD']
    return jumlah
def EUR_ke_IDR(jumlah) :
    jumlah = jumlah* kurs.kurses['EUR']
    return jumlah
def SGD_ke_IDR(jumlah) :
    jumlah = jumlah * kurs.kurses['SGD']
    return jumlah
def JPY_ke_IDR(jumlah) :
    jumlah = jumlah * kurs.kurses['JPY']
    return jumlah

#memindahkan kurs idr ke kurs lain
def IDR_ke_USD(jumlah) :
    jumlah = jumlah / kurs.kurses['USD']
    return jumlah
def IDR_ke_EUR(jumlah) :
    jumlah = jumlah / kurs.kurses['EUR']
    return jumlah
def IDR_ke_SGD(jumlah) :
    jumlah = jumlah / kurs.kurses['SGD']
    return jumlah
def IDR_ke_JPY(jumlah) :
    jumlah = jumlah/ kurs.kurses['JPY']
    return jumlah