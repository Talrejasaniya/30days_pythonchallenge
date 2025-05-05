# Define the structure of a Node
class Node:
    def __init__(self, data):
        self.data = data        # Store the data value
        self.next = None        # Pointer to the next node (initially None)

# Class to handle linked list operations
class Solution: 
    def display(self, head):
        # Print all nodes in the linked list
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Insert a new node at the end of the list
        new_node = Node(data)           # Create a new node
        if head is None:                # If list is empty, return new node as head
            return new_node
        else:
            current = head
            while current.next:         # Traverse to the end of the list
                current = current.next
            current.next = new_node     # Link the new node at the end
            return head                 # Return the unchanged head

# Driver code
mylist = Solution()
T = int(input())              # Number of elements to insert
head = None

for i in range(T):
    data = int(input())       # Read each data element
    head = mylist.insert(head, data)  # Insert into the linked list

mylist.display(head)          # Display the linked list
