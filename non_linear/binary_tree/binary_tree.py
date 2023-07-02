class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    