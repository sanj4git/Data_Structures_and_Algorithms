class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def isLeafNode(self):
        if self is None:
            return False
        if self.left is None and self.right is None:
            return True
        else:
            return False
    
    def isInternalNode(self):
        if self is None:
            return False
        if self.left is not None or self.right is not None:
            return True
        else:
            return False
    
    def isExternalNode(self):
        if self is None:
            return False
        if self.left is None and self.right is None:
            return True
        else:
            return False
    
    def isLeftNode(self):
        if self is None:
            return False
        if self.parent is None:
            return False
        if self.parent.left is None:
            return False
        if self.parent.left == self:
            return True
        else:
            return False

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.size += 1
        else:
            # Iterative
            currentNode = self.root
            while True:
                if data <= currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = Node(data)
                        currentNode.left.parent = currentNode
                        self.size += 1
                        break
                    else:
                        currentNode = currentNode.left
                elif data > currentNode.data:
                    if currentNode.right is None:
                        currentNode.right = Node(data)
                        currentNode.right.parent = currentNode
                        self.size += 1
                        break
                    else:
                        currentNode = currentNode.right
        
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
    
    def search(self, data):
        if self.root is None:
            return False
        else:
            currentNode = self.root
            while True:
                if currentNode is None:
                    return False
                elif data == currentNode.data:
                    return True
                elif data < currentNode.data:
                    currentNode = currentNode.left
                elif data > currentNode.data:
                    currentNode = currentNode.right
    
    def height(self, node):
        if node is None:
            return -1
        else:
            leftHeight = self.height(node.left)
            rightHeight = self.height(node.right)
            return max(leftHeight, rightHeight) + 1
    
    def isBalanced(self, node):
        if node is None:
            return True
        else:
            leftHeight = self.height(node.left)
            rightHeight = self.height(node.right)

            if abs(leftHeight - rightHeight) <= 1 and self.isBalanced(node.left) and self.isBalanced(node.right):
                return True
            else:
                return False

    def levelOrder(self, node):
        if node is None:
            return []

        queue = []
        queue.append(node)
        queue.append(None)

        levelOrderList = [[]]
        level = 0

        while len(queue) > 0:
            currentNode = queue.pop(0)
            if currentNode is None:
                level += 1
                if len(queue) > 0:
                    levelOrderList.append([])
                    queue.append(None)
            else:
                levelOrderList[level].append(currentNode.data)
                
                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)
        
        return levelOrderList
    
    # Level Order starts from 1
    def getNodesAtLevel(self, level):
        if self.root is None:
            return []
        else:
            levelOrderList = self.levelOrder(self.root)
            if level > len(levelOrderList):
                return []
            else:
                return levelOrderList[level-1]
    
    def spiralOrder(self, node):
        if node is None:
            return []
        else:
            levelOrderList = self.levelOrder(node)
            spiralOrderList = []
            for i in range(len(levelOrderList)):
                if i % 2 != 0:
                    levelOrderList[i].reverse()
                spiralOrderList.append(levelOrderList[i])
            return spiralOrderList
    
    def mirrorImage(self, node):
        if node is None:
            return
        else:
            levelOrderList = self.levelOrder(node)
            for i in range(len(levelOrderList)):
                levelOrderList[i].reverse()
            return levelOrderList
    
    def lowestCommonAncestor(self, nodeA, nodeB):
        if self.root is None:
            return None
        else:
            if self.search(nodeA) == False or self.search(nodeB) == False:
                return None
            currentNode = self.root
            while True:
                if currentNode.data > nodeA and currentNode.data > nodeB:
                    currentNode = currentNode.left
                elif currentNode.data < nodeA and currentNode.data < nodeB:
                    currentNode = currentNode.right
                else:
                    return currentNode.data
    
    def greatestCommonAncestor(self, nodeA, nodeB):
        if not self.search(nodeA) or not self.search(nodeB):
            return None

        currentNode = self.root
        if nodeA <= currentNode.data and nodeB <= currentNode.data:
            return self.root.data
        if nodeA > currentNode.data and nodeB > currentNode.data:
            return self.lowestCommonAncestor(nodeA, nodeB)
        
        return self.root.data

    def kThMinimum(self, k):
        if self.root is None or k >= self.size:
            return None
        
        return self.inOrder(self.root)[k - 1]
    
    def kThMaximum(self, k):
        if self.root is None or k >= self.size:
            return None
        
        inOrder = self.inOrder(self.root)
        inOrder.reverse()
        
        return inOrder[k-1]
    
    def levelOrderNodeList(self, node):
        if node is None:
            return []
        else:
            queue = []
            queue.append(node)
            queue.append(None)

            levelOrderList = [[]]
            level = 0

            while len(queue) > 0:
                currentNode = queue.pop(0)
                if currentNode is None:
                    level += 1
                    if len(queue) > 0:
                        levelOrderList.append([])
                        queue.append(None)
                else:
                    levelOrderList[level].append(currentNode)
                    
                    if currentNode.left is not None:
                        queue.append(currentNode.left)
                    if currentNode.right is not None:
                        queue.append(currentNode.right)
            
            return levelOrderList
    
    def deepestLeftLeaf(self, node : Node):
        levelOrder = self.levelOrderNodeList(node)
        if levelOrder is {}:
            return None
        for level in range(len(levelOrder) - 1, -1, -1):
            for node in levelOrder[level]:
                if node.isLeafNode() and node.isLeftNode():
                    return node.data
                
        return None
    
    def inOrderSuccessor(self, node):
        currentNode = node
        while currentNode and currentNode.left != None:
            currentNode = currentNode.left
        
        return currentNode
    
    def delete(self, node, key):
        if key < node.data:
            node.left = self.delete(node.left, key)
        
        elif key > node.data:
            node.right = self.delete(node.right, key)
        
        else:
            # Case 1. No children.
            # Case 2. 1 child.
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp
            
            # Case 3. Two children.
            temp = self.inOrderSuccessor(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)
        
        return node



bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(17)
bst.insert(16)
bst.insert(18)

print("In Order: ", bst.inOrder(bst.root))
print("Pre Order: ", bst.preOrder(bst.root))
print("Post Order: ", bst.postOrder(bst.root))
print("Search 10: ", bst.search(10))
print("Height: ", bst.height(bst.root))
print("Is Balanced: ", bst.isBalanced(bst.root))
print("Level Order: ", bst.levelOrder(bst.root))
print("Nodes at Level 3: ", bst.getNodesAtLevel(3))
print("Spiral Order: ", bst.spiralOrder(bst.root))
print("Mirror Image: ", bst.mirrorImage(bst.root))
print("Lowest Common Ancestor of 3 and 7: ", bst.lowestCommonAncestor(3, 7))
print("Greatest Common Ancestor of 3 and 7: ", bst.greatestCommonAncestor(3, 7))
print("Kth Minimum (k = 3): ", bst.kThMinimum(3))
print("Kth Maximum (k = 3): ", bst.kThMaximum(3))
print("Deepest Left Leaf: ", bst.deepestLeftLeaf(bst.root))

bstB = BST()

bstB.root = Node(44)
bstB.root.left = Node(17)
bstB.root.right = Node(88)
bstB.root.left.left = Node(8)
bstB.root.left.right = Node(28)
bstB.root.left.right.left = Node(21)
bstB.root.left.right.right = Node(29)

bstB.root.right.left = Node(65)
bstB.root.right.right = Node(97)
bstB.root.right.right.left = Node(93)

bstB.root.right.left.left = Node(54)
bstB.root.right.left.right = Node(82)
bstB.root.right.left.right.left = Node(76)
bstB.root.right.left.right.left.left = Node(68)
bstB.root.right.left.right.left.right = Node(80)

print("InOrder:", bstB.inOrder(bstB.root))
print("Delete 88", bstB.delete(bstB.root, 88))
print("InOrder:", bstB.inOrder(bstB.root))