class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            return
        
        currentNode = self.head
        while currentNode.next != self.head:
            currentNode = currentNode.next

        currentNode.next = newNode
        newNode.next = self.head
    
    def insert_first(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            return
        
        currentNode = self.head
        while currentNode.next != self.head:
            currentNode = currentNode.next

        currentNode.next = newNode
        newNode.next = self.head
        self.head = newNode

    def search(self, key):
        if self.head is None:
            return False
        if self.head.data == key:
            return True
        currentNode = self.head.next
        while currentNode != self.head:
            if currentNode.data == key:
                return True
            currentNode = currentNode.next
        return False
    
    def insert_after(self, key, data):
        if self.head is None:
            return False
        if self.head.data == key:
            newNode = Node(data)
            newNode.next = self.head.next
            self.head.next = newNode
            return True
        currentNode = self.head.next
        while currentNode != self.head:
            if currentNode.data == key:
                newNode = Node(data)
                newNode.next = currentNode.next
                currentNode.next = newNode
                return True
            currentNode = currentNode.next
        return False
    
    def insert_before(self, key, data):
        if self.head is None:
            return False
        if self.head.data == key:
            newNode = Node(data)
            newNode.next = self.head
            currentNode = self.head
            while currentNode.next != self.head:
                currentNode = currentNode.next
            currentNode.next = newNode
            self.head = newNode
            return True
        currentNode = self.head
        while currentNode.next != self.head:
            if currentNode.next.data == key:
                newNode = Node(data)
                newNode.next = currentNode.next
                currentNode.next = newNode
                return True
            currentNode = currentNode.next
        return False
    
    def delete(self, key):
        if self.head is None:
            return False
        if self.head.data == key:
            currentNode = self.head
            while currentNode.next != self.head:
                currentNode = currentNode.next
            currentNode.next = self.head.next
            self.head = self.head.next
            return True
        currentNode = self.head
        while currentNode.next != self.head:
            if currentNode.next.data == key:
                currentNode.next = currentNode.next.next
                return True
            currentNode = currentNode.next
        return False
    
    def delete_first(self):
        if self.head is None:
            return False
        if self.head.next == self.head:
            self.head = None
            return True
        currentNode = self.head
        while currentNode.next != self.head:
            currentNode = currentNode.next
        currentNode.next = self.head.next
        self.head = self.head.next
        return True
    
    def delete_last(self):
        if self.head is None:
            return False
        if self.head.next == self.head:
            self.head = None
            return True
        currentNode = self.head
        while currentNode.next.next != self.head:
            currentNode = currentNode.next
        currentNode.next = self.head
        return True
    
    def print_list(self):
        if self.head is None:
            return
        currentNode = self.head
        while True:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
            if currentNode == self.head:
                break
        print()

circularLinkedList = CircularLinkedList()
circularLinkedList.insert_last(1)
circularLinkedList.insert_last(2)
circularLinkedList.insert_last(3)
circularLinkedList.insert_last(4)
circularLinkedList.insert_last(5)
circularLinkedList.insert_last(6)
circularLinkedList.insert_last(7)

circularLinkedList.print_list()

circularLinkedList.insert_first(0)
circularLinkedList.insert_first(-1)
circularLinkedList.insert_first(-2)

circularLinkedList.print_list()

print(circularLinkedList.search(0))
print(circularLinkedList.search(10))

circularLinkedList.insert_after(0, 10)
circularLinkedList.insert_after(10, 11)

circularLinkedList.print_list()

circularLinkedList.insert_before(0, -10)

circularLinkedList.print_list()

circularLinkedList.delete(0)
circularLinkedList.delete(11)
circularLinkedList.delete(10)

circularLinkedList.print_list()

circularLinkedList.delete_first()

circularLinkedList.print_list()

circularLinkedList.delete_last()

circularLinkedList.print_list()

