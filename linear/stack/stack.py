class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
        print("Stack is empty")
        return None

    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def print_stack(self):
        if not self.is_empty():
            for item in self.items:
                print(item, end=" ")
            print()
        else:
            print("Stack is empty")

st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)

st.print_stack()

st.pop()

st.print_stack()

st.pop()
st.pop()
st.pop()

st.print_stack()

st.pop()

st.print_stack()
