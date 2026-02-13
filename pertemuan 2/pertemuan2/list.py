thislist = ["mango", "strawberry", "kiwi"]
print(thislist)

# allow duplicates
thislist = ["mango", "strawberry", "kiwi", "mango", "kiwi"]
print(thislist)

# list length
thislist = ["mango", "strawberry", "kiwi"]
print(len(thislist))

#Daftar Item - Tipe Data
list1 = ["manggo", "strawberry", "kiwi"]#string
list2 = [1, 5, 7, 9, 3]#integer
list3 = [True, False, False]#boolean
print(list1)
print(list2)
print(list3)

# type()
mylist = ["manggo", "strawberry", "kiwi"]
print(type(mylist))

# konstruktor list()
thislist = list(("manggo", "strawberry", "kiwi")) # note the double round-brackets
print(thislist)

# mengakses item list
thislist = ["manggo", "strawberry", "kiwi"]
print(thislist[1])

# mengakses item list negatif
thislist = ["manggo", "strawberry", "kiwi"]
print(thislist[-1])

# rentang indeks\
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[3:6])

# rentaang indeks negatif
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-6:-2])

#check if item exists
thislist = ["manggo", "strawberry", "kiwi"]
if "manggo" in thislist:
  print("Yes, 'manggo' is in the fruits list")


#mengubah item list
thislist = ["apple", "banana", "cherry"]

thislist[1] = "strawberry"
print(thislist)

# mengubah beberapa item list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[2:4] = ["strawberry", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# appand()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# inesrt items
thislist = ["strawberry","banana","cherry"]
thislist.insert(3, "orange")
print(thislist)

thislist = ["apple", "strawberry", "cherry"]
buah_buahan = ["mango", "pineapple", "papaya"]
thislist.extend(buah_buahan)
print(thislist)

thislist = ["apple", "strawberry", "cherry"]
thislist.remove("strawberry")
print(thislist)

thislist = ["apple", "strawberry", "cherry"]
thislist.pop(2)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "strawberry", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "strawberry", "cherry"]
[print(x) for x in thislist]

#tanpa list compereshion
fruits = ["strawberry", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#menggunakan list compereshion
fruits = ["strawbery", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# newlist = [expression for item in iterable if condition == True]

# Condition
newlist = [x for x in fruits if x != "apple"]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if x != "apple"]

print(newlist)


#iterable
newlist = [x for x in range(10)]
newlist = [x for x in range(10)]
print(newlist)


#expression
newlist = [x.upper() for x in fruits]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x if x != "strawberry" else "orange" for x in fruits]
fruits = ["apple", "strawberry", "cherry", "kiwi", "mango"]

newlist = [x if x != "strawberry" else "banana" for x in fruits]

print(newlist)

# sort  list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)

thislist = ["apple", "strawberry", "cherry", "kiwi", "mango"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 55)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["apple", "strawberry", "cherry", "kiwi", "mango"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#menggunakan append
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#menggunakan exetend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)