class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(Node):
    def __init__(self, root):
        self.root = Node(root)

    def printTree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preOrderTraversal(self.root, "")
        elif traversal_type =="inorder":
            return self.inOrderTraversal(self.root, "")
        elif traversal_type =="postorder":
            return self.postOrderTraversal(self.root, "")
        else:
            print(f"traversal type {traversal_type} is not supported")
            return False
        
    def preOrderTraversal(self, start, traversal):
        # root-> left-> right
        if start:
            traversal += str(start.value)
            traversal = self.preOrderTraversal(start.left, traversal)
            traversal = self.preOrderTraversal(start.right, traversal) 
        
        return traversal
    
    def inOrderTraversal(self, start, traversal):
        #left -> root -> right
        if start:
            traversal = self.inOrderTraversal(start.left, traversal)
            traversal += str(start.value)
            traversal = self.inOrderTraversal(start.right, traversal)
        
        return traversal
    
    def postOrderTraversal(self, start, traversal):
        # left -> right -> root
        if start:
            traversal = self.postOrderTraversal(start.left, traversal)
            traversal = self.postOrderTraversal(start.right, traversal)
            traversal += str(start.value)
        return traversal
        
    #      1
    #    /   \
    #   2     3
    #  /
    # 4
# Set up
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)

print(tree.printTree("preorder"))
print(tree.printTree("inorder"))
print(tree.printTree("postorder"))


