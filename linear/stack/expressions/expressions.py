# InFix: a + (( b * c ) / d )
# PostFix: a b c * d / +
# PreFix: + a / * b c d

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
        return None

    def is_empty(self):
        return self.stack == []
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
        return None
    
    def top(self):
        if not self.is_empty():
            return self.stack[0]
        
        return None
    
    def print_stack(self):
        if not self.is_empty():
            for item in self.stack:
                print(item, end=" ")
            print()
        else:
            print("Stack is empty")

def is_operator(c):
    if c == "+" or c == "-" or c == "*" or c == "/" or c == "^":
        return True
    else:
        return False

def is_operand(c):
    if c.isalpha() or c.isdigit():
        return True
    else:
        return False

def precedence(c):
    if c == "^":
        return 3
    elif c == "*" or c == "/":
        return 2
    elif c == "+" or c == "-":
        return 1
    else:
        return 0

def infix_to_postfix(infix):
    postfix = ""
    stack = Stack()

    for c in infix:
        if is_operand(c):
            postfix += c
        elif c == "(":
            stack.push(c)
        elif c == ")":
            while (not stack.is_empty()) and (stack.peek() != "("):
                postfix += stack.pop()
            stack.pop()
        elif is_operator(c):
            while (not stack.is_empty()) and (precedence(c) <= precedence(stack.peek())):
                postfix += stack.pop()
            stack.push(c)
        
    while not stack.is_empty():
        postfix += stack.pop()
    
    return postfix

def infix_to_prefix(infix):
    prefix = ""
    stack = Stack()

    for c in infix[::-1]:
        if is_operand(c):
            prefix += c
        elif c == ")":
            stack.push(c)
        elif c == "(":
            while (not stack.is_empty()) and (stack.peek() != ")"):
                prefix += stack.pop()
            stack.pop()
        elif is_operator(c):
            while (not stack.is_empty()) and (precedence(c) < precedence(stack.peek())):
                prefix += stack.pop()
            stack.push(c)
    
    while not stack.is_empty():
        prefix += stack.pop()
    
    return prefix[::-1]

def postfix_to_infix(postfix):
    infix = ""
    stack = Stack()

    for c in postfix:
        if is_operand(c):
            stack.push(c)
        elif is_operator(c):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push("(" + op2 + c + op1 + ")")
    
    infix = stack.pop()
    return infix

def prefix_to_infix(prefix):
    infix = ""
    stack = Stack()

    for c in prefix[::-1]:
        if is_operand(c):
            stack.push(c)
        elif is_operator(c):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push("(" + op1 + c + op2 + ")")
    
    infix = stack.pop()
    return infix

def prefix_to_postfix(prefix):
    postfix = ""
    stack = Stack()

    for c in prefix[::-1]:
        if is_operand(c):
            stack.push(c)
        elif is_operator(c):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(op1 + op2 + c)
    
    postfix = stack.pop()
    return postfix

def postfix_to_prefix(postfix):
    prefix = ""
    stack = Stack()

    for c in postfix:
        if is_operand(c):
            stack.push(c)
        elif is_operator(c):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(c + op2 + op1)
    
    prefix = stack.pop()
    return prefix

print()
print("[InFix]: a + (( b * c ) / d )")
print()
print("[In -> Post]: ",infix_to_postfix("a+((b*c)/d)"))
print("[In -> Pre]: ", infix_to_prefix("a+((b*c)/d)"))
print()
print("[Post -> In]: ", postfix_to_infix(infix_to_postfix("a+((b*c)/d)")))
print("[Post -> Pre]", postfix_to_prefix(infix_to_postfix("a+((b*c)/d)")))
print()
print("[Pre -> In]", prefix_to_infix(infix_to_prefix("a+((b*c)/d)")))
print("[Pre -> Post]", prefix_to_postfix(infix_to_prefix("a+((b*c)/d)")))