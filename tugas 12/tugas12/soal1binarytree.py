#class node
class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#class binary tree
class BinaryTree:
    def __init__(self):
        self.root = None

    #fungsi untuk memasukkan data secara manual
    def insert_manual(self, data):
        self.root = Node(data)
    
    def insert_left(self, parent_node, data):
        if parent_node.left is not None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
    
    def insert_right(self, parent_node, data):
        if parent_node.right is not None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

struktur_gudang = BinaryTree()  


#  struktur tree-nya 
#        A
#       / \
#      B   C
#     / \   \
#    D   E   F

#membuat struktur tree secara manual sesuai dengan struktur di atas
struktur_gudang.insert_manual("A")
struktur_gudang.insert_left(struktur_gudang.root, "B")
struktur_gudang.insert_left(struktur_gudang.root.left, "D")
struktur_gudang.insert_right(struktur_gudang.root.left, "E")
struktur_gudang.insert_right(struktur_gudang.root, "C")
struktur_gudang.insert_right(struktur_gudang.root.right, "F")

#fungsi traversal preorder (root - left - right)
def traverse_preorder(node):
    if node is not None:
        print(node.data, end=" - ")
        traverse_preorder(node.left)
        traverse_preorder(node.right)

#fungsi traversal inorder (left - root - right)
def traverse_inorder(node):
    if node is not None:
        traverse_inorder(node.left)
        print(node.data, end=" - ")
        traverse_inorder(node.right)

#fungsi traversal postorder (left - right - root)
def traverse_postorder(node):
    if node is not None:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print(node.data, end=" - ")

#fungsi untuk mengambil leaf nodes (gudang ujung)
def get_leaf_nodes(node):
    if node is None:
        return []
    
    if node.left is None and node.right is None:
        return [node.data]
    
    return get_leaf_nodes(node.left) + get_leaf_nodes(node.right)


#main program-nya 
print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("======================================")
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.")

print("\nHASIL AUDIT:")
print("1. Pre-Order  : ", end=" ")
traverse_preorder(struktur_gudang.root)
print("\n2. In-Order   : ", end=" ")
traverse_inorder(struktur_gudang.root)
print("\n3. Post-Order : ", end=" ")
traverse_postorder(struktur_gudang.root)

print("\n")
print(f"[DATA] Gudang Ujung (Leaf Nodes): {get_leaf_nodes(struktur_gudang.root)}")
print("======================================")
print("Audit Selesai!")