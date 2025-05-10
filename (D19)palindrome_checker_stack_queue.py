class Solution:
    def __init__(self):
        # Initialize separate containers for stack and queue
        self.stack = []
        self.queue = []

    # Push character onto the stack (LIFO)
    def pushCharacter(self, ch):
        self.stack = [ch] + self.stack  # Insert at the beginning

    # Enqueue character into the queue (FIFO)
    def enqueueCharacter(self, ch):
        self.queue.append(ch)  # Insert at the end

    # Pop character from the stack
    def popCharacter(self):
        return self.stack.pop(0)  # Remove from the beginning

    # Dequeue character from the queue
    def dequeueCharacter(self):
        front = self.queue[0]    # Get the front element
        self.queue = self.queue[1:]  # Remove it
        return front

# Read input from user
s = input()

# Create an object of Solution class
obj = Solution()

# Add each character to both stack and queue
for ch in s:
    obj.pushCharacter(ch)
    obj.enqueueCharacter(ch)

# Check for palindrome
isPalindrome = True
for i in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

# Print the result
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
