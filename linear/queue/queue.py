class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        
        print("Queue is empty")
        return None
    
    def is_empty(self):
        return self.queue == []
    
    def first(self):
        if not self.is_empty():
            return self.queue[0]
        
        return None
    
    def print_queue(self):
        if not self.is_empty():
            for item in self.queue:
                print(item, end=" ")
            print()
        else:
            print("Queue is empty")
    
    def size(self):
        return len(self.queue)

q = Queue()

q.enqueue(5)
q.enqueue(3)

q.print_queue()

q.dequeue()

q.print_queue()

q.enqueue(2)
q.enqueue(8)

q.print_queue()

q.dequeue()
q.dequeue()

q.print_queue()

print(q.is_empty())

q.enqueue(9)
q.enqueue(1)

q.print_queue()

q.dequeue()

q.print_queue()

q.enqueue(7)
q.enqueue(6)

q.print_queue()

print(q.first())

q.dequeue()
q.dequeue()

q.print_queue()

q.enqueue(4)

q.print_queue()

q.dequeue()
q.dequeue()

q.print_queue()