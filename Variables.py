#Creating Variables
#Membuat Variabel
Q = 5
P = "Doni"
print(Q)
print(P)

#Casting
x = str(27)    
y = int(6)    
z = float(23)

#Get the Type
x = 7
y = "Ayam"
print(type(x))
print(type(y))

#Single or Double Quotes(satu atau 2 tanda kutip)
x = "ikan"
x = 'ikan'

#Case-Sensitive
d = 23
D = "Jelly"
print(d)
print(D)

#Variable Names
#Nama variabel yang sah
myvar = "Jennie"
my_var = "Jennie"
_my_var = "Jennie"
myVar = "Jennie"
MYVAR = "Jennie"
myvar2 = "Jennie"

#Multi Words Variable Names
#Camel Case(java gunain ini)
#Setiap kata, kecuali kata pertama, diawali dengan huruf kapital
myVariableName = "Jennie"

#Pascal Case
#Setiap kata diawali dengan huruf kapital
MyVariableName = "Jennie"

#Snake Case (python gunain ini)
#Setiap kata dipisahkan oleh karakter garis bawah
my_variable_name = "Jennie"

#Banyak Nilai untuk Banyak Variabel
x, y, z = "apel", "Berry", "Cherry"
print(x)
print(y)
print(z)

#Satu Nilai untuk Beberapa Variabel
x = y = z = "blueberry"
print(x)
print(y)
print(z)

#Unpack a Collection(membuka koleksi)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Variabel Output
#Variabel Keluaran
A = "exo akan comeback"
print(A)

b = "exo"
c = "akan"
d = "comeback"
print(b, c, d)

b = "exo "
c = "akan "
d = "comback"
print(b + c + d)

#Global Variables
#Variabel Global 
#Buat variabel di luar fungsi, dan gunakan variabel tersebut di dalam fungsi
G = "Amazing"

def myfunc():
  print("Python is " + G)

myfunc()

#Buat variabel di dalam fungsi, dengan nama yang sama dengan variabel global.
G = "Amazing"

def myfunc():
  G = "fantastic"
  print("gruop exo " + G)

myfunc()

print("gruop exo " + G)

#The global Keyword(Kata kunci global)
#Jika Anda menggunakan globalkata kunci tersebut, variabel tersebut termasuk dalam cakupan global
def myfunc():
  global j
  j = "dunia"

myfunc()

print("indahnya " + j)

#Untuk mengubah nilai variabel global di dalam sebuah fungsi, rujuk variabel tersebut dengan menggunakan globalkata kunci
k = "keeren"

def myfunc():
  global k
  k = "mantab"

myfunc()

print("Python is " + k)
