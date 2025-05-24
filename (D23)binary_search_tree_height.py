class Node:
    def __init__(self, data):
        self.right = self.left = None  # Initialize left and right child as None
        self.data = data               # Store the node’s value

class Solution:
    def insert(self, root, data):
        # If tree/subtree is empty, create a new node and return it
        if root is None:
            return Node(data)
        else:
            # If data is less or equal, insert into left subtree
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                # Else insert into right subtree
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        # Base case: empty subtree has height -1
        if root is None:
            return -1

        # Recursively get height of left subtree
        left = self.getHeight(root.left)
        # Recursively get height of right subtree
        right = self.getHeight(root.right)

        # Height of current node = 1 + max height of left/right subtree
        return 1 + max(left, right)

# Number of nodes to insert
T = int(input())
myTree = Solution()
root = None

# Insert nodes one by one into the BST
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

# Compute and print the height of the tree
height = myTree.getHeight(root)
print(height)
