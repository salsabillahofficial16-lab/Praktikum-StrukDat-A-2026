# Bagian A — Double Linked List

class Node :
    def __init__(self,judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul):
            new_node = Node(judul,None)

            if self.head is None:
                self.head = new_node
                return

            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
            new_node.prev = current
    
    def display_forward(self):
        current = self.head
        while current:
            print(current.judul, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head

        while current and current.next:
            current = current.next

        while current:
            print(current.judul, end=" <-> ")
            current = current.prev
        print("None")

    def delete(self, judul):
        current = self.judul

        while current:
            if current.judul == judul:
                if current.prev is None:
                    self.judul = current.next
                    if self.judul:
                        self.judul.prev = None
                else:
                    current.prev.next = current.next

                    if current.next:
                        current.next.prev = current.prev
                return

            current = current.next

buku = DoublyLinkedList()

buku.insert_tail('Laskar Pelangi')
buku.insert_tail('bumi manusia')
buku.insert_tail('sang pemimpi')


buku.display_backward()
buku.display_forward()

# Bagian B — Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_list(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.nex

        new_node.next = self.head
        current.next = new_node
        self.head = new_node
  
    def delete_head(self, data):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            if current.data == data:
  
                if current == self.head and current.next == self.head:
                    self.head = None

                elif current == self.head:
                    last = self.head
   
                    while last.next != self.head:
                        last = last.next
           
                    self.head = self.head.next
        
                    last.next = self.head
                    
                else:
                    
                    prev.next = current.next

                return

            prev = current
            current = current.next

            if current == self.head:
                break

    def display(self):
        if self.head is None:
            print("Linked list kosong")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(kembali ke head)")



pelanggan = CircularLinkedList()
pelanggan.insert_list('Andi')
pelanggan.insert_list('budi')
pelanggan.insert_list('dina')

pelanggan.insert_list('Edo')
pelanggan.display()

pelanggan.delete_head('Andi')

pelanggan.display()