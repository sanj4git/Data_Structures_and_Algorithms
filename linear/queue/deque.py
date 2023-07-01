class Deque:
    def __init__(self):
        self.deque = []
    
    def insertFirst(self, item):
        self.deque.insert(0, item)
    
    def insertLast(self, item):
        self.deque.append(item)
    
    def deleteFirst(self):
        if not self.isEmpty():
            return self.deque.pop(0)
        
        print("Deque is empty")
        return None

    def deleteLast(self):
        if not self.isEmpty():
            return self.deque.pop()
        
        print("Deque is empty")
        return None
    
    def isEmpty(self):
        return self.deque == []
    
    def first(self):
        if not self.isEmpty():
            return self.deque[0]
        
        return None
    
    def last(self):
        if not self.isEmpty():
            return self.deque[-1]
        
        return None
    
    def printDeque(self):
        if not self.isEmpty():
            for item in self.deque:
                print(item, end=" ")
            print()
        else:
            print("Deque is empty")

dq = Deque()

