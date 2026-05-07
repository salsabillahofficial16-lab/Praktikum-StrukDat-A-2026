#class node untuk menyimpan data buku dan judulnya
class Node:
    def __init__ (self, data, judul):
        self.data = data
        self.judul = judul
        self.left = None
        self.right = None

#class binary sort tree untuk menyimpan data buku dan judulnya dengan struktur binary search tree
class BinarySortTree:
    def __init__(self):
        self.root = None
    
    def insert (self, data, judul):
        #langkah 1
        new = Node (data, judul)
        #langkah 2
        if self.root is None:
            #jika iya
            self.root = new
            print(f"[INSERT] BERHASIL MEMASUKKAN : id {data} - {judul}")
            return
        
        #langkah 3
        P = self.root
        Q = self.root

        #langkah 4
        while Q is not None and new.data != P.data:
            #langkah 5
            P = Q

            #langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right
        
        #langkah 7
        if new.data == P.data:
            print("datanya duplikat")
            return

        #langkah 8
        if new.data < P.data:
            P.left = new

        else:
            P.right = new

        print(f"[INSERT] BERHASIL MEMASUKKAN : id {data} - {judul}")

    #fungsi untuk mencari data buku berdasarkan id
    def search (self, data):
        Searching_ = self.root
        while Searching_ is not None:
            if data == Searching_.data:
                return Searching_
            
            if data < Searching_.data:
                Searching_ = Searching_.left

            else:
                Searching_ = Searching_.right
        return None
    
    #fungsi untuk mencari id terkecil dan terbesar dalam tree
    def get_min(self):
            if self.root is None:
                return None
            
            Min_ = self.root
            while Min_.left is not None:
                Min_ = Min_.left
            return Min_.data
    
    #fungsi untuk mencari id terbesar dalam tree
    def get_max(self):
        Max_ = self.root
        while Max_.right is not None:
            Max_ = Max_.right
        return Max_.data
    
    #fungsi untuk menghitung tinggi tree
    def height(self, node):
        if node is None:
            return -1
        left_hight = self.height(node.left)
        right_hight = self.height(node.right)

        if left_hight > right_hight:
            return left_hight + 1
        else:
            return right_hight +1

#fungsi untuk melakukan traversal inorder (left - root - right)
def Traversal_in_order(self, node):
     if node is not None:
        self.Traversal_in_order(node.left)
        print(node.data, "-", node.judul)
        self.Traversal_in_order(node.right)
        
data_buku = BinarySortTree()




#main programnya
print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=======================================================")


data_buku.insert(50, "Dasar Pemograman")
data_buku.insert(30, "Struktur Data")
data_buku.insert(70, "Kecerdasan Buatan")
data_buku.insert(20, "Matematika Diskrit")
data_buku.insert(40, "Basis Data")
data_buku.insert(60, "Jaringan Komputer")
data_buku.insert(80, "Sistem Operasi")

print("\n[INFO] Koleksi Buku (In-Order Traversal):", end= " ")
data_buku.Traversal_in_order(data_buku.root)

print("\n[SEARCH] mencari id 60...", end=" ")

judul_1= data_buku.search(60)
if judul_1 is not None:
    print(f"Ditemuan! Judul: ", judul_1.judul )
else: 
    print(f"Data tidak ditemukan.")

print("[SEARCH] mencari id 100...", end=" ")

judul_2= data_buku.search(100)
if judul_2 is not None:
    print(f"Ditemuan! Judul: ", judul_2.judul )
else: 
    print(f"Data tidak ditemukan.")


print(f"\n[STATISTIK] id TERKECIL: ",data_buku.get_min())
print(f"[STATISTIK] id TERBESAR: ",data_buku.get_max())

Tinggi = data_buku.height(data_buku.root)
print(f"[INFO] Tinggi (Height) Tree: {Tinggi}")
print("=========================================")
print("Simulasi selesai!")



