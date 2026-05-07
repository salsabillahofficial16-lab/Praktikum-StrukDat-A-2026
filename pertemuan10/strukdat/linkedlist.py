# List Biasa
# from inspect import stack


class StackList:
 def __init__(self):
  self.items = [] 

 def is_empty(self, URL):
    return len(self.items) == 0
#  isEmpty = not bool(self.items)

 def push(self, URL):
# Tulis kode di sini (Petunjuk: gunakan append)
   self.items.append(URL)
 
 def pop(self):
# Tulis kode di sini (Petunjuk: pastikan tidak kosong, lalu gunakan pop)
  if self.is_empty():
   return "stack is empty"
  
  return self.items.pop()

 
 def peek(self,):
# Tulis kode di sini (Petunjuk: kembalikan elemen indeks terakhir [-1])    
  if self.is_empty():
    return "stack is empty"
    
  return self.items[-1]   

 def size(self):
# Tulis kode di sini (Petunjuk: gunakan len())
   return len(self.items)

StackList1 = StackList()
StackList1.push('saasaa.com')
StackList1.push('sasa.com')
StackList1.push('sasa.com')

print("StackList1ack: ", StackList1.items)
print("Size: ", StackList1.size())
print("Peek: ", StackList1.peek())
print("Pop: ", StackList1.pop())
print("Stack: ", StackList1.items)


# Linked List
class Node:
 def __init__(self, url):
  self.url = url
  self.next = None

class StackLinkedList:
  def __init__(self):
   self.top = None
   self.count = 0 

def is_empty(self):
    return self.count == 0

def push(self, URL):
     new_node = Node(URL)
     if self.top:
      new_node.next = self.top
     self.top = new_node
     self.count += 1

def pop(self):
    if self.is_empty():
      return "stack is empty"
    popped_node = self.top
    self.top = self.top.next
    self.count -= 1
    return popped_node.url


def peek(self):
    if self.is_empty():
        return "stack is empty"
    return self.top.url

def size(self):
    return self.count

def traverse(self):
    currentNode = self.top
    urls = []
    while currentNode:
        urls.append(currentNode.url)
        currentNode = currentNode.next
    return urls

StackLinkedList2  = StackLinkedList()
StackLinkedList2.push('saasaa.com')
StackLinkedList2.push('sasa.com')
StackLinkedList2.push('sasa.com')

print("Stack: ", StackLinkedList.traverse())
print("Size: ", StackLinkedList.size())
print("Peek: ", StackLinkedList.peek())
print("Pop: ", StackLinkedList.pop())
print("is Empty: ", StackLinkedList.is_empty())