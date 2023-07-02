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

    def buildTreeFromPreIn(self, preOrder, inOrder):
        if len(preOrder) == 0:
            return None

        root = Node(preOrder[0])
        rootIndex = inOrder.index(preOrder[0])

        root.left = self.buildTreeFromPreIn(preOrder[1:rootIndex+1], inOrder[:rootIndex])
        root.right = self.buildTreeFromPreIn(preOrder[rootIndex+1:], inOrder[rootIndex+1:])

        return root
    
    def buildTreeFromPostIn(self, post, ino):
        if len(post) == 0:
            return None

        root = Node(post[-1])
        rootIndex = ino.index(post[-1])

        root.left = self.buildTreeFromPostIn(post[:rootIndex], ino[:rootIndex])
        root.right = self.buildTreeFromPostIn(post[rootIndex:-1], ino[rootIndex+1:])

        return root
        
    
    def inOrder(self, node):
        if node is None:
            return []
        return self.inOrder(node.left) + [node.data] + self.inOrder(node.right)

    def preOrder(self, node):
        if node is None:
            return []
        return [node.data] + self.preOrder(node.left) + self.preOrder(node.right)
    
    def postOrder(self, node):
        if node is None:
            return []
        return self.postOrder(node.left) + self.postOrder(node.right) + [node.data]

preOrder = [1, 2, 4, 5, 3, 6, 7]
inOrder = [4, 2, 5, 1, 6, 3, 7]

treeA = BinaryTree()
treeA.root = treeA.buildTreeFromPreIn(preOrder, inOrder)

print("InOrder: ", treeA.inOrder(treeA.root))
print("PreOrder: ", treeA.preOrder(treeA.root))
print("PostOrder: ", treeA.postOrder(treeA.root))

print("====================================")

postOrder = [4, 5, 2, 6, 7, 3, 1]
inOrder = [4, 2, 5, 1, 6, 3, 7]

treeB = BinaryTree()
treeB.root = treeB.buildTreeFromPostIn(postOrder, inOrder)

print("InOrder: ", treeB.inOrder(treeB.root))
print("PreOrder: ", treeB.preOrder(treeB.root))
print("PostOrder: ", treeB.postOrder(treeB.root))
