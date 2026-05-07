print("\nList Biasa")
class StackList:
    def __init__(self):
        self.items = []
  
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items[-1]
  
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

MyStackList = StackList()

MyStackList.push('sasaa.com')
MyStackList.push('sasa.com')
MyStackList.push('mssa.com')

print("Stack: ", MyStackList.items)
print("Pop: ", MyStackList.pop())
print("Stack after Pop: ", MyStackList.items)
print("Peek: ", MyStackList.peek())
print("isEmpty: ", MyStackList.isEmpty())
print("Size: ", MyStackList.size())

print("\nLinked List")
class Node:
  def __init__(self, url):
    self.url = url
    self.next = None

class StackLinkedList:
  def __init__(self):
    self.top = None
    self.count = 0

  def push(self, url):
    new_node = Node(url)
    if self.top:
      new_node.next = self.top
    self.top = new_node
    self.count += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.top
    self.top = self.top.next
    self.count -= 1
    return popped_node.url

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.top.url

  def isEmpty(self):
    return self.count == 0

  def stackSize(self):
    return self.count

  def traverseAndPrint(self):
    currentNode = self.top
    while currentNode:
      print(currentNode.url, end=" -> ")
      currentNode = currentNode.next
    print()

myStackLinked = StackLinkedList()

myStackLinked.push('sasa.com')
myStackLinked.push('asa.com')
myStackLinked.push('sasaa.com')

print("LinkedList: ", end="")
myStackLinked.traverseAndPrint()
print("Peek: ", myStackLinked.peek())
print("Pop: ", myStackLinked.pop())
print("LinkedList after Pop: ", end="")
myStackLinked.traverseAndPrint()
print("isEmpty: ", myStackLinked.isEmpty())
print("Size: ", myStackLinked.stackSize())