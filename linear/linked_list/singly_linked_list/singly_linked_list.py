class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = newNode

    def insert_first(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        newNode.next = self.head
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
            self.head = newNode
            return True
        currentNode = self.head
        while currentNode.next:
            if currentNode.next.data == key:
                newNode = Node(data)
                newNode.next = currentNode.next
                currentNode.next = newNode
                return True
            currentNode = currentNode.next
        return False
    
    def delete_nth_occurence(self, key, n):
        currentNode = self.head
        count = 1
        prev = None
        while currentNode:
            if currentNode.data == key:
                if count == n:
                    if prev is None:
                        self.head = currentNode.next
                    else:
                        prev.next = currentNode.next
                    return True
                count += 1
            prev = currentNode
            currentNode = currentNode.next
        return False
    
    def delete_first(self):
        if self.head is None:
            return False
        self.head = self.head.next
        return True
    
    def delete_last(self):
        if self.head is None:
            return False
        if self.head.next is None:
            self.head = None
            return True
        currentNode = self.head
        while currentNode.next.next:
            currentNode = currentNode.next
        currentNode.next = None
        return True
    
    def delete_all_occurences(self, key):
        if self.head is None:
            return False
        while self.head and self.head.data == key:
            self.head = self.head.next
        currentNode = self.head
        while currentNode.next:
            if currentNode.next.data == key:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return True
    
    def print_list(self):
        if self.head is None:
            print('List is empty')
            return
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print()
    

sll = SLL()

sll.insert_last(1)
sll.insert_last(2)
sll.insert_last(3)
sll.insert_last(4)
sll.insert_last(5)
sll.insert_last(6)
sll.insert_last(7)

sll.insert_first(0)
sll.insert_first(0)
sll.insert_first(0)

sll.print_list()

print(sll.search(0))
print(sll.search(1))
print(sll.search(2))
print(sll.search(3))
print(sll.search(4))

print(sll.delete_nth_occurence(0, 1))
print(sll.delete_nth_occurence(0, 1))
print(sll.delete_nth_occurence(0, 1))

sll.print_list()

print(sll.delete_first())
print(sll.delete_first())
print(sll.delete_first())

sll.print_list()

print(sll.delete_last())
print(sll.delete_last())
print(sll.delete_last())

sll.print_list()

print(sll.delete_all_occurences(1))

sll.print_list()