class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_last(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def insert_first(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
    
    def search(self, key):
        currentNode = self.head
        while currentNode:
            if currentNode.data == key:
                return True
            currentNode = currentNode.next
        return False
    
    def insert_after(self, key, data):
        currentNode = self.head
        while currentNode:
            if currentNode.data == key:
                newNode = Node(data)
                newNode.prev = currentNode
                newNode.next = currentNode.next
                currentNode.next = newNode
                if newNode.next:
                    newNode.next.prev = newNode
                else:
                    self.tail = newNode
                return True
            currentNode = currentNode.next
        return False
    
    def insert_before(self, key, data):
        if self.head is None:
            return False
        if self.head.data == key:
            newNode = Node(data)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return True
        currentNode = self.head
        while currentNode.next:
            if currentNode.next.data == key:
                newNode = Node(data)
                newNode.prev = currentNode
                newNode.next = currentNode.next
                currentNode.next = newNode
                newNode.next.prev = newNode
                return True
            currentNode = currentNode.next
        return False
    
    def delete(self, key):
        if self.head is None:
            return False
        if self.head.data == key:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return True
        currentNode = self.head
        while currentNode.next:
            if currentNode.next.data == key:
                currentNode.next = currentNode.next.next
                if currentNode.next:
                    currentNode.next.prev = currentNode
                else:
                    self.tail = currentNode
                return True
            currentNode = currentNode.next
        return False
    
    def delete_first(self):
        if self.head is None:
            return False
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return True
    
    def delete_last(self):
        if self.head is None:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return True
        self.tail = self.tail.prev
        self.tail.next = None
        return True
    
    def print_list(self):
        if self.head is None:
            print("Empty list")
            return
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print()

dll = DLL()
dll.insert_last(1)
dll.insert_last(2)
dll.insert_last(3)
dll.insert_last(4)

dll.print_list()

dll.insert_first(0)
dll.insert_first(-1)
dll.insert_first(-2)

dll.print_list()

print(dll.search(0))

dll.insert_after(0, 0.5)

dll.print_list()

dll.insert_before(0, -0.5)

dll.print_list()

dll.delete(0)

dll.print_list()

dll.delete_first()

dll.print_list()

dll.delete_last()

dll.print_list()

dll.delete_last()

dll.print_list()
