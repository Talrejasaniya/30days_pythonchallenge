# Node class to define structure of each linked list node
class Node:
    def __init__(self, data):
        self.data = data       # Value of the node
        self.next = None       # Pointer to the next node

# Solution class containing all linked list operations
class Solution: 
    # Method to insert a new node at the end of the list
    def insert(self, head, data):
        p = Node(data)           
        if head == None:        # If list is empty, new node is head
            head = p
        elif head.next == None: # If only one node, add to next
            head.next = p
        else:
            start = head
            while(start.next != None):  # Traverse to the end
                start = start.next
            start.next = p              # Append new node at the end
        return head  
    
    # Method to display all values in the linked list
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')  # Print data of each node
            current = current.next

    # Method to remove duplicate values from the linked list
    def removeDuplicates(self, head):
        if head == None:
            return head

        seen = set()             # Set to store already seen values
        current = head
        seen.add(current.data)   # Add head data to set

        while current.next:      # Loop through list
            if current.next.data in seen:
                current.next = current.next.next  # Skip duplicate node
            else:
                seen.add(current.next.data)       # Add new value to set
                current = current.next            # Move to next node
        return head

# Driver code
mylist = Solution()
T = int(input())                 # Number of elements to insert
head = None
for i in range(T):
    data = int(input())         # Input each value
    head = mylist.insert(head, data)    

head = mylist.removeDuplicates(head)  # Remove duplicates
mylist.display(head)                  # Print final list
