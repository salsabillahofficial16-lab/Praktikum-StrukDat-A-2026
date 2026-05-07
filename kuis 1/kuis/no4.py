def hitung_diskon(total_belanja, level_diskon, index=0):
    level_diskon = (
(500000, 15), # belanja >= 500.000 -> diskon 15%
(300000, 10), # belanja >= 300.000 -> diskon 10%
(100000, 5), # belanja >= 100.000 -> diskon 5%
(0, 0), # default -> tidak ada diskon
)
    return level_diskon

# cek_diskon= (int("persen_diskon", "nominal_diskon", "total_bayar"))
belanjaan = []
for i in range(2):
    print(f"=== menghitung jumlah belanjaan ===")
    total_belanja = (int(input("total_belanja :")))
    level_diskon  = (int(input("level_diskon :")))
    belanjaan = hitung_diskon(float('level_diskon'))


if belanjaan >=  500.000:
    print("diskon 15%")
elif belanjaan >= 300.000:
   print("diskon 10%")
elif belanjaan >= 100.000:
    print("diskon 5%")
else:
    print("tidak ada diskon!")

print("hitung_diskon")
print(f"=== selesai ===")