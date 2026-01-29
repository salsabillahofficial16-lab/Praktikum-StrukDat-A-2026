#Tipe Data Python
#Tipe Data Bawaan
#tipe data python =
#Variabel dapat menyimpan data dengan tipe yang berbeda, dan tipe yang berbeda dapat melakukan hal yang berbeda pula,
#Python memiliki tipe data bawaan berikut secara default
#tipe data python =
# Jenis Teks    :	str
# Tipe Numerik  :	int, float, complex
# Jenis Urutan  :	list, tuple, range
# Jenis Pemetaan:	dict
# Jenis Set     :	set,frozenset
# Tipe Boolean  :	bool
# Tipe Biner    :	bytes, bytearray, memoryview
# Tidak ada Tipe:	NoneType

#Mendapatkan Tipe Data (Getting the Data Type)
#Cetak tipe data variabel x:

x = 5
print(type(x))

#Mengatur Tipe Data
#Dalam Python, tipe data ditentukan saat Anda memberikan nilai ke sebuah variabel
# Contoh                                       Data Type
# x = "Hello World"	                            str	
# x = 20	                                    int	
# x = 20.5	                                    float	
# x = 1j	                                    complex	
# x = ["apple", "banana", "cherry"]	            list	
# x = ("apple", "banana", "cherry")	            tuple	
# x = range(6)	                                range	
# x = {"name" : "John", "age" : 36}	            dict	
# x = {"apple", "banana", "cherry"}	            set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	                                    bool	
# x = b"Hello"                                	bytes	
# x = bytearray(5)                            	bytearray	
# x = memoryview(bytes(5))	                    memoryview	
# x = None	                                    NoneType	

# Menetapkan Tipe Data Spesifik
# Jika Anda ingin menentukan tipe data, Anda dapat menggunakan fungsi konstruktor berikut:

# contoh	                                                           Data Type
# x = str("Hello World")	                                              str	
# x = int(20)	                                                          int	
# x = float(20.5)                                                       float	
# x = complex(1j)	                                                      complex	
# x = list(("apple", "banana", "cherry"))                            	  list	
# x = tuple(("apple", "banana", "cherry"))	                          tuple	
# x = range(6)	                                                      range	
# x = dict(name="John", age=36)	                                      dict	
# x = set(("apple", "banana", "cherry"))                    	          set	
# x = frozenset(("apple", "banana", "cherry"))	                      frozenset	
# x = bool(5)	                                                          bool	
# x = bytes(5)   	                                                      bytes	
# x = bytearray(5)	                                                  bytearray	
# x = memoryview(bytes(5))	                                          memoryview