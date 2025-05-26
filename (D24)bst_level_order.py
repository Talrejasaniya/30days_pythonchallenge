# Define the Node class to build the binary search tree (BST)
class Node:
    def __init__(self, data):
        self.left = None          # Pointer to left child
        self.right = None         # Pointer to right child
        self.data = data          # Value stored in this node

# Define the Solution class that contains insertion and traversal logic
class Solution:
    
    # Insert a value into the BST
    def insert(self, root, data):
        if root is None:
            return Node(data)     # Create a new node if current root is None
        else:
            if data <= root.data:
                # Insert in the left subtree
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                # Insert in the right subtree
                cur = self.insert(root.right, data)
                root.right = cur
        return root               # Return the updated tree

    # Perform Level Order Traversal (Breadth-First Search)
    def levelOrder(self, root):
        if root is None:
            return
        
        queue = [root]  # Initialize queue with the root node

        while queue:
            current = queue.pop(0)            # Remove the front node from queue
            print(current.data, end=' ')      # Print the node's value

            if current.left:
                queue.append(current.left)    # Add left child to queue

            if current.right:
                queue.append(current.right)   # Add right child to queue

# Read number of nodes to insert
T = int(input())

myTree = Solution()
root = None

# Insert all nodes
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

# Print level order traversal
myTree.levelOrder(root)
